// website/src/components/atlas/AtlasExplorer.tsx
import React, { useState, useEffect, useCallback, useMemo } from 'react';
import type { AtlasGraphData, AtlasNode, AtlasTrail } from '../../lib/atlas/types';
import { AtlasToolbar } from './AtlasToolbar';
import { AtlasMap } from './AtlasMap';
import { AtlasList } from './AtlasList';
import { AtlasFolio } from './AtlasFolio';
import { AtlasTrailBar } from './AtlasTrailBar';
import { AtlasSearchModal } from './AtlasSearchModal';

interface Props {
  initialGraph: AtlasGraphData;
  initialFocusNodeId?: string | null;
  initialTrailId?: string | null;
}

export const AtlasExplorer: React.FC<Props> = ({
  initialGraph,
  initialFocusNodeId = null,
  initialTrailId = null,
}) => {
  const { regions, nodes, edges, trails } = initialGraph;

  // State management
  const [focusedNodeId, setFocusedNodeId] = useState<string | null>(initialFocusNodeId);
  const [activeTrailId, setActiveTrailId] = useState<string | null>(initialTrailId);
  const [currentTrailStopIndex, setCurrentTrailStopIndex] = useState(0);
  const [selectedRegion, setSelectedRegion] = useState<string | null>(null);
  const [filterKind, setFilterKind] = useState<string | null>(null);
  const [viewMode, setViewMode] = useState<'map' | 'list'>('map');
  const [searchOpen, setSearchOpen] = useState(false);
  const [isFolioOpen, setIsFolioOpen] = useState(Boolean(initialFocusNodeId));

  // Map viewport transform state
  const [zoomLevel, setZoomLevel] = useState(0.95);
  const [panOffset, setPanOffset] = useState({ x: 0, y: 0 });

  // Bookmarks state (Local storage backed)
  const [bookmarkedNodeIds, setBookmarkedNodeIds] = useState<Set<string>>(new Set());

  // Personal exploration journey thread state (The Thread)
  const [userThreadNodeIds, setUserThreadNodeIds] = useState<string[]>([]);

  // Node lookup map
  const nodeMap = useMemo(() => new Map(nodes.map((n) => [n.id, n])), [nodes]);
  const trailMap = useMemo(() => new Map(trails.map((t) => [t.id, t])), [trails]);

  // Load bookmarks & thread on mount
  useEffect(() => {
    try {
      const saved = localStorage.getItem('hiyu_atlas_bookmarks');
      if (saved) {
        setBookmarkedNodeIds(new Set(JSON.parse(saved)));
      }
      const savedThread = localStorage.getItem('hiyu_atlas_thread');
      if (savedThread) {
        setUserThreadNodeIds(JSON.parse(savedThread));
      }
    } catch (e) {
      // Ignore
    }
  }, []);

  // Sync URL search params on mount
  useEffect(() => {
    if (typeof window === 'undefined') return;
    const params = new URLSearchParams(window.location.search);
    const focusParam = params.get('focus');
    const trailParam = params.get('trail');
    const viewParam = params.get('view');
    const regionParam = params.get('region');

    if (focusParam) {
      const found = nodes.find((n) => n.id === focusParam || n.slug === focusParam);
      if (found) {
        setFocusedNodeId(found.id);
        setIsFolioOpen(true);
      }
    }

    if (trailParam) {
      const foundTrail = trails.find((t) => t.id === trailParam || t.slug === trailParam);
      if (foundTrail) {
        setActiveTrailId(foundTrail.id);
        setCurrentTrailStopIndex(0);
        if (foundTrail.orderedNodeIds.length > 0) {
          setFocusedNodeId(foundTrail.orderedNodeIds[0]);
          setIsFolioOpen(true);
        }
      }
    }

    if (viewParam === 'list') setViewMode('list');
    if (regionParam) setSelectedRegion(regionParam);
  }, [nodes, trails]);

  // Update URL search params cleanly without reload
  const updateUrlState = useCallback(
    (focusId: string | null, trailId: string | null, mode: 'map' | 'list') => {
      if (typeof window === 'undefined') return;
      const params = new URLSearchParams(window.location.search);

      if (focusId) {
        const node = nodeMap.get(focusId);
        params.set('focus', node ? node.slug : focusId);
      } else {
        params.delete('focus');
      }

      if (trailId) {
        const trail = trailMap.get(trailId);
        params.set('trail', trail ? trail.slug : trailId);
      } else {
        params.delete('trail');
      }

      if (mode === 'list') {
        params.set('view', 'list');
      } else {
        params.delete('view');
      }

      const newUrl = `${window.location.pathname}${params.toString() ? '?' + params.toString() : ''}`;
      window.history.replaceState(null, '', newUrl);
    },
    [nodeMap, trailMap]
  );

  // Center map on a node
  const centerOnNode = useCallback((node: AtlasNode) => {
    // Coordinate space is 1000x1000. Center is at (500, 500)
    const targetX = (500 - node.visual.x) * 0.8;
    const targetY = (500 - node.visual.y) * 0.8;
    setPanOffset({ x: targetX, y: targetY });
    setZoomLevel(1.35);
  }, []);

  // Handle node selection (with Thread tracking)
  const handleSelectNode = useCallback(
    (nodeId: string) => {
      setFocusedNodeId(nodeId);
      setIsFolioOpen(true);
      updateUrlState(nodeId, activeTrailId, viewMode);

      // Etch step into User's personal exploration Thread
      setUserThreadNodeIds((prev) => {
        if (prev.length > 0 && prev[prev.length - 1] === nodeId) return prev;
        const next = [...prev, nodeId];
        try {
          localStorage.setItem('hiyu_atlas_thread', JSON.stringify(next));
        } catch (e) {}
        return next;
      });

      const target = nodeMap.get(nodeId);
      if (target && viewMode === 'map') {
        centerOnNode(target);
      }
    },
    [activeTrailId, viewMode, nodeMap, updateUrlState, centerOnNode]
  );

  const handleClearThread = useCallback(() => {
    setUserThreadNodeIds([]);
    try {
      localStorage.removeItem('hiyu_atlas_thread');
    } catch (e) {}
  }, []);

  // Handle closing folio
  const handleCloseFolio = useCallback(() => {
    setIsFolioOpen(false);
    setFocusedNodeId(null);
    updateUrlState(null, activeTrailId, viewMode);
  }, [activeTrailId, viewMode, updateUrlState]);

  // Handle bookmark toggle
  const handleToggleBookmark = useCallback((nodeId: string) => {
    setBookmarkedNodeIds((prev) => {
      const next = new Set(prev);
      if (next.has(nodeId)) {
        next.delete(nodeId);
      } else {
        next.add(nodeId);
      }
      try {
        localStorage.setItem('hiyu_atlas_bookmarks', JSON.stringify([...next]));
      } catch (e) {}
      return next;
    });
  }, []);

  // Keyboard shortcuts (⌘K for search, + / - / 0 for zoom)
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      // Don't trigger shortcuts if user is typing in an input or textarea
      const target = e.target as HTMLElement;
      if (target.tagName === 'INPUT' || target.tagName === 'TEXTAREA' || target.isContentEditable) {
        return;
      }

      if ((e.metaKey || e.ctrlKey) && e.key === 'k') {
        e.preventDefault();
        setSearchOpen((prev) => !prev);
      } else if (e.key === '+' || e.key === '=') {
        e.preventDefault();
        setZoomLevel((z) => Math.min(3.0, z * 1.2));
      } else if (e.key === '-' || e.key === '_') {
        e.preventDefault();
        setZoomLevel((z) => Math.max(0.6, z * 0.8));
      } else if (e.key === '0') {
        e.preventDefault();
        setZoomLevel(0.95);
        setPanOffset({ x: 0, y: 0 });
      }
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, []);

  // Active Trail logic
  const activeTrail = activeTrailId ? trailMap.get(activeTrailId) : null;
  const currentTrailNode =
    activeTrail && activeTrail.orderedNodeIds[currentTrailStopIndex]
      ? nodeMap.get(activeTrail.orderedNodeIds[currentTrailStopIndex]) || null
      : null;

  const handleStartTrail = useCallback(
    (trailId: string) => {
      const trail = trailMap.get(trailId);
      if (!trail) return;
      setActiveTrailId(trail.id);
      setCurrentTrailStopIndex(0);
      setViewMode('map');

      const firstNodeId = trail.orderedNodeIds[0];
      if (firstNodeId) {
        handleSelectNode(firstNodeId);
      }
      updateUrlState(firstNodeId, trail.id, 'map');
    },
    [trailMap, handleSelectNode, updateUrlState]
  );

  const handleNextTrailStop = useCallback(() => {
    if (!activeTrail) return;
    if (currentTrailStopIndex < activeTrail.orderedNodeIds.length - 1) {
      const nextIndex = currentTrailStopIndex + 1;
      setCurrentTrailStopIndex(nextIndex);
      const nextNodeId = activeTrail.orderedNodeIds[nextIndex];
      handleSelectNode(nextNodeId);
    }
  }, [activeTrail, currentTrailStopIndex, handleSelectNode]);

  const handlePrevTrailStop = useCallback(() => {
    if (!activeTrail) return;
    if (currentTrailStopIndex > 0) {
      const prevIndex = currentTrailStopIndex - 1;
      setCurrentTrailStopIndex(prevIndex);
      const prevNodeId = activeTrail.orderedNodeIds[prevIndex];
      handleSelectNode(prevNodeId);
    }
  }, [activeTrail, currentTrailStopIndex, handleSelectNode]);

  const handleCloseTrail = useCallback(() => {
    setActiveTrailId(null);
    setCurrentTrailStopIndex(0);
    updateUrlState(focusedNodeId, null, viewMode);
  }, [focusedNodeId, viewMode, updateUrlState]);

  // Zoom helpers
  const handleZoomIn = () => setZoomLevel((z) => Math.min(3.0, z * 1.2));
  const handleZoomOut = () => setZoomLevel((z) => Math.max(0.6, z * 0.8));
  const handleResetZoom = () => {
    setZoomLevel(0.95);
    setPanOffset({ x: 0, y: 0 });
  };

  const focusedNode = focusedNodeId ? nodeMap.get(focusedNodeId) || null : null;

  return (
    <div className="relative w-full h-full flex-1 flex flex-col bg-bg text-text overflow-hidden">
      {/* Top Instrument Toolbar */}
      <AtlasToolbar
        regions={regions}
        trails={trails}
        selectedRegion={selectedRegion}
        onSelectRegion={setSelectedRegion}
        filterKind={filterKind}
        onSelectFilterKind={setFilterKind}
        viewMode={viewMode}
        onToggleViewMode={(mode) => {
          setViewMode(mode);
          updateUrlState(focusedNodeId, activeTrailId, mode);
        }}
        onOpenSearch={() => setSearchOpen(true)}
        onZoomIn={handleZoomIn}
        onZoomOut={handleZoomOut}
        onResetZoom={handleResetZoom}
        onStartTrail={handleStartTrail}
      />

      {/* Main Exploration Surface */}
      <div className="relative flex-1 w-full h-full overflow-hidden">
        {viewMode === 'map' ? (
          <AtlasMap
            nodes={nodes}
            edges={edges}
            regions={regions}
            focusedNodeId={focusedNodeId}
            onSelectNode={handleSelectNode}
            selectedRegion={selectedRegion}
            filterKind={filterKind}
            zoomLevel={zoomLevel}
            panOffset={panOffset}
            onPanChange={setPanOffset}
            onZoomChange={setZoomLevel}
            userThreadNodeIds={userThreadNodeIds}
            onClearThread={handleClearThread}
          />
        ) : (
          <div className="w-full h-full overflow-y-auto">
            <AtlasList
              nodes={nodes}
              regions={regions}
              onSelectNode={handleSelectNode}
              focusedNodeId={focusedNodeId}
              selectedRegion={selectedRegion}
              filterKind={filterKind}
            />
          </div>
        )}

        {/* Guided Exhibition Trail Dock */}
        {activeTrail && (
          <AtlasTrailBar
            trail={activeTrail}
            currentStopIndex={currentTrailStopIndex}
            currentNode={currentTrailNode}
            onNextStop={handleNextTrailStop}
            onPrevStop={handlePrevTrailStop}
            onCloseTrail={handleCloseTrail}
          />
        )}
      </div>

      {/* Slide-out Museum Folio Drawer */}
      <AtlasFolio
        node={focusedNode}
        isOpen={isFolioOpen}
        onClose={handleCloseFolio}
        onSelectNode={handleSelectNode}
        isBookmarked={focusedNode ? bookmarkedNodeIds.has(focusedNode.id) : false}
        onToggleBookmark={handleToggleBookmark}
        threadStep={userThreadNodeIds.indexOf(focusedNodeId || '') + 1}
      />

      {/* ⌘K Fast Search Modal */}
      <AtlasSearchModal
        isOpen={searchOpen}
        onClose={() => setSearchOpen(false)}
        onSelectNode={handleSelectNode}
      />
    </div>
  );
};
