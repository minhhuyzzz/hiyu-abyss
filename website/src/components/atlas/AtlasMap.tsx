// website/src/components/atlas/AtlasMap.tsx
import React, { useRef, useState, useEffect, useCallback } from 'react';
import type { AtlasNode, AtlasEdge, AtlasRegion } from '../../lib/atlas/types';

interface Props {
  nodes: AtlasNode[];
  edges: AtlasEdge[];
  regions: AtlasRegion[];
  focusedNodeId: string | null;
  onSelectNode: (nodeId: string) => void;
  selectedRegion: string | null;
  filterKind: string | null;
  zoomLevel: number;
  panOffset: { x: number; y: number };
  onPanChange: (offset: { x: number; y: number }) => void;
  onZoomChange: (level: number) => void;
}

export const AtlasMap: React.FC<Props> = ({
  nodes,
  edges,
  regions,
  focusedNodeId,
  onSelectNode,
  selectedRegion,
  filterKind,
  zoomLevel,
  panOffset,
  onPanChange,
  onZoomChange,
}) => {
  const containerRef = useRef<HTMLDivElement>(null);
  const [isDragging, setIsDragging] = useState(false);
  const [dragStart, setDragStart] = useState({ x: 0, y: 0 });
  const [hoveredNodeId, setHoveredNodeId] = useState<string | null>(null);

  // Map node lookup by ID
  const nodeMap = useRef(new Map<string, AtlasNode>());
  useEffect(() => {
    nodeMap.current = new Map(nodes.map((n) => [n.id, n]));
  }, [nodes]);

  // Identify connected node IDs when a node is hovered or focused
  const activeNodeId = hoveredNodeId || focusedNodeId;
  const connectedNodeIds = React.useMemo(() => {
    if (!activeNodeId) return new Set<string>();
    const ids = new Set<string>();
    ids.add(activeNodeId);
    for (const e of edges) {
      if (e.from === activeNodeId) ids.add(e.to);
      if (e.to === activeNodeId) ids.add(e.from);
    }
    return ids;
  }, [activeNodeId, edges]);

  // Mouse pan handlers
  const handleMouseDown = (e: React.MouseEvent) => {
    if ((e.target as HTMLElement).closest('[data-node-button]')) return;
    setIsDragging(true);
    setDragStart({ x: e.clientX - panOffset.x, y: e.clientY - panOffset.y });
  };

  const handleMouseMove = (e: React.MouseEvent) => {
    if (!isDragging) return;
    onPanChange({
      x: e.clientX - dragStart.x,
      y: e.clientY - dragStart.y,
    });
  };

  const handleMouseUp = () => {
    setIsDragging(false);
  };

  // Wheel zoom handler
  const handleWheel = (e: React.WheelEvent) => {
    e.preventDefault();
    const zoomFactor = e.deltaY < 0 ? 1.12 : 0.88;
    const newZoom = Math.max(0.6, Math.min(3.0, zoomLevel * zoomFactor));
    onZoomChange(newZoom);
  };

  // Touch pan & pinch zoom handlers
  const touchStartRef = useRef<{ dist: number; x: number; y: number } | null>(null);

  const handleTouchStart = (e: React.TouchEvent) => {
    if (e.touches.length === 1) {
      setIsDragging(true);
      setDragStart({
        x: e.touches[0].clientX - panOffset.x,
        y: e.touches[0].clientY - panOffset.y,
      });
    } else if (e.touches.length === 2) {
      const dist = Math.hypot(
        e.touches[0].clientX - e.touches[1].clientX,
        e.touches[0].clientY - e.touches[1].clientY
      );
      touchStartRef.current = {
        dist,
        x: (e.touches[0].clientX + e.touches[1].clientX) / 2,
        y: (e.touches[0].clientY + e.touches[1].clientY) / 2,
      };
    }
  };

  const handleTouchMove = (e: React.TouchEvent) => {
    if (e.touches.length === 1 && isDragging) {
      onPanChange({
        x: e.touches[0].clientX - dragStart.x,
        y: e.touches[0].clientY - dragStart.y,
      });
    } else if (e.touches.length === 2 && touchStartRef.current) {
      const dist = Math.hypot(
        e.touches[0].clientX - e.touches[1].clientX,
        e.touches[0].clientY - e.touches[1].clientY
      );
      const factor = dist / touchStartRef.current.dist;
      const newZoom = Math.max(0.6, Math.min(3.0, zoomLevel * factor));
      onZoomChange(newZoom);
      touchStartRef.current.dist = dist;
    }
  };

  const handleTouchEnd = () => {
    setIsDragging(false);
    touchStartRef.current = null;
  };

  // Get active hovered node data for tooltip
  const hoveredNode = hoveredNodeId ? nodeMap.current.get(hoveredNodeId) : null;

  return (
    <div
      ref={containerRef}
      onMouseDown={handleMouseDown}
      onMouseMove={handleMouseMove}
      onMouseUp={handleMouseUp}
      onMouseLeave={handleMouseUp}
      onWheel={handleWheel}
      onTouchStart={handleTouchStart}
      onTouchMove={handleTouchMove}
      onTouchEnd={handleTouchEnd}
      className={`relative w-full h-full overflow-hidden select-none bg-bg text-text ${
        isDragging ? 'cursor-grabbing' : 'cursor-grab'
      }`}
    >
      {/* Decorative Vintage Compass Rose Ornament in Corner */}
      <div className="absolute top-4 left-4 pointer-events-none z-10 opacity-40 hidden sm:block">
        <svg width="80" height="80" viewBox="0 0 100 100" className="text-accent stroke-current fill-none">
          <circle cx="50" cy="50" r="42" strokeWidth="0.8" strokeDasharray="2 2" />
          <circle cx="50" cy="50" r="36" strokeWidth="0.5" />
          <path d="M50 8 L53 45 L50 50 L47 45 Z" fill="currentColor" opacity="0.8" />
          <path d="M50 92 L53 55 L50 50 L47 55 Z" fill="currentColor" opacity="0.4" />
          <path d="M8 50 L45 47 L50 50 L45 53 Z" fill="currentColor" opacity="0.4" />
          <path d="M92 50 L55 47 L50 50 L55 53 Z" fill="currentColor" opacity="0.4" />
          <text x="50" y="6" textAnchor="middle" fontSize="6" fontFamily="serif" fill="currentColor">N</text>
          <text x="96" y="52" textAnchor="middle" fontSize="6" fontFamily="serif" fill="currentColor">E</text>
          <text x="50" y="99" textAnchor="middle" fontSize="6" fontFamily="serif" fill="currentColor">S</text>
          <text x="4" y="52" textAnchor="middle" fontSize="6" fontFamily="serif" fill="currentColor">W</text>
        </svg>
      </div>

      {/* Main SVG Celestial Map Viewport */}
      <svg
        viewBox="0 0 1000 1000"
        className="w-full h-full transition-transform duration-75 ease-out will-change-transform"
        style={{
          transform: `translate(${panOffset.x}px, ${panOffset.y}px) scale(${zoomLevel})`,
          transformOrigin: '50% 50%',
        }}
      >
        <defs>
          {/* Subtle Celestial Radial Gradients */}
          <radialGradient id="celestial-plate-glow" cx="50%" cy="50%" r="50%">
            <stop offset="0%" stopColor="var(--accent)" stopOpacity="0.08" />
            <stop offset="60%" stopColor="var(--accent)" stopOpacity="0.02" />
            <stop offset="100%" stopColor="transparent" stopOpacity="0" />
          </radialGradient>

          <radialGradient id="node-active-halo" cx="50%" cy="50%" r="50%">
            <stop offset="0%" stopColor="var(--accent)" stopOpacity="0.4" />
            <stop offset="100%" stopColor="var(--accent)" stopOpacity="0" />
          </radialGradient>

          {/* Region Halos */}
          {regions.map((r) => (
            <radialGradient key={r.id} id={`halo-${r.id}`} cx="50%" cy="50%" r="50%">
              <stop offset="0%" stopColor={r.colorToken} stopOpacity="0.12" />
              <stop offset="80%" stopColor={r.colorToken} stopOpacity="0.02" />
              <stop offset="100%" stopColor={r.colorToken} stopOpacity="0" />
            </radialGradient>
          ))}
        </defs>

        {/* 1. Background Celestial Plate Grids & Rings */}
        <rect width="1000" height="1000" fill="url(#celestial-plate-glow)" />

        {/* Antique Concentric Astrolabe Coordinate Rings */}
        <g className="text-accent/20 stroke-current fill-none pointer-events-none" strokeWidth="0.75">
          <circle cx="500" cy="500" r="160" strokeDasharray="3 3" />
          <circle cx="500" cy="500" r="310" strokeDasharray="2 4" />
          <circle cx="500" cy="500" r="460" strokeWidth="1" />
          <circle cx="500" cy="500" r="485" strokeWidth="0.5" strokeDasharray="1 2" />

          {/* Crosshair meridians */}
          <line x1="500" y1="20" x2="500" y2="980" strokeDasharray="4 4" strokeWidth="0.5" />
          <line x1="20" y1="500" x2="980" y2="500" strokeDasharray="4 4" strokeWidth="0.5" />

          {/* Roman Degree Labels */}
          <text x="500" y="35" textAnchor="middle" fontSize="9" fontFamily="serif" fill="currentColor">XII · ZENITH</text>
          <text x="500" y="975" textAnchor="middle" fontSize="9" fontFamily="serif" fill="currentColor">VI · NADIR</text>
          <text x="965" y="503" textAnchor="end" fontSize="9" fontFamily="serif" fill="currentColor">III · ORIENS</text>
          <text x="35" y="503" textAnchor="start" fontSize="9" fontFamily="serif" fill="currentColor">IX · OCCIDENS</text>
        </g>

        {/* 2. 8 Curated Regions: Halos & Constellation Titles */}
        <g className="pointer-events-none">
          {regions.map((region) => {
            const isRegionSelected = !selectedRegion || selectedRegion === region.id;
            return (
              <g
                key={region.id}
                className="transition-opacity duration-300"
                style={{ opacity: isRegionSelected ? 1 : 0.2 }}
              >
                {/* Region Territory Halo */}
                <circle
                  cx={region.centerCoordinates.x}
                  cy={region.centerCoordinates.y}
                  r="180"
                  fill={`url(#halo-${region.id})`}
                />
                <circle
                  cx={region.centerCoordinates.x}
                  cy={region.centerCoordinates.y}
                  r="180"
                  stroke={region.colorToken}
                  strokeWidth="0.5"
                  strokeDasharray="4 6"
                  opacity="0.25"
                  fill="none"
                />

                {/* Region Title Plate */}
                <text
                  x={region.centerCoordinates.x}
                  y={region.centerCoordinates.y - 120}
                  textAnchor="middle"
                  fontFamily="Cormorant Garamond, serif"
                  fontSize="13"
                  letterSpacing="1.5"
                  fill={region.colorToken}
                  opacity="0.85"
                  className="font-medium uppercase"
                >
                  {region.astronomyGlyph} {region.label}
                </text>
                <text
                  x={region.centerCoordinates.x}
                  y={region.centerCoordinates.y - 106}
                  textAnchor="middle"
                  fontFamily="Literata, serif"
                  fontSize="8"
                  fontStyle="italic"
                  fill="#9E998F"
                  opacity="0.6"
                >
                  {region.label_en}
                </text>
              </g>
            );
          })}
        </g>

        {/* 3. Constellation Edges (118 Curated Connections) */}
        <g>
          {edges.map((edge) => {
            const source = nodeMap.current.get(edge.from);
            const target = nodeMap.current.get(edge.to);
            if (!source || !target) return null;

            const isConnectedToActive =
              activeNodeId && (edge.from === activeNodeId || edge.to === activeNodeId);
            const isFaded = activeNodeId && !isConnectedToActive;

            // Stroke styling based on relation
            let strokeColor = '#C29A77';
            let strokeDash = undefined;
            if (edge.relation === 'contrasts_with') {
              strokeColor = '#B47862'; // Oxide
              strokeDash = '4 3';
            } else if (edge.relation === 'influenced_by') {
              strokeColor = '#96A79A'; // Patina
              strokeDash = '2 2';
            }

            const strokeOpacity = isConnectedToActive ? 0.9 : isFaded ? 0.04 : 0.18;
            const strokeWidth = isConnectedToActive ? 1.8 : 0.75;

            // Slight curve calculation for elegance
            const midX = (source.visual.x + target.visual.x) / 2;
            const midY = (source.visual.y + target.visual.y) / 2;
            const dx = target.visual.x - source.visual.x;
            const dy = target.visual.y - source.visual.y;
            // perpendicular displacement
            const offsetDist = Math.min(25, Math.hypot(dx, dy) * 0.08);
            const perpX = midX - (dy / Math.hypot(dx, dy)) * offsetDist;
            const perpY = midY + (dx / Math.hypot(dx, dy)) * offsetDist;

            const pathD = `M ${source.visual.x} ${source.visual.y} Q ${perpX} ${perpY} ${target.visual.x} ${target.visual.y}`;

            return (
              <g key={edge.id} className="transition-all duration-200">
                <path
                  d={pathD}
                  fill="none"
                  stroke={strokeColor}
                  strokeWidth={strokeWidth}
                  strokeDasharray={strokeDash}
                  strokeOpacity={strokeOpacity}
                />
                {/* Active Directional Glow Bead */}
                {isConnectedToActive && (
                  <circle
                    cx={perpX}
                    cy={perpY}
                    r="2.5"
                    fill={strokeColor}
                    opacity="0.85"
                  />
                )}
              </g>
            );
          })}
        </g>

        {/* 4. Nodes (86 Curated Celestial Medallions) */}
        <g>
          {nodes.map((node) => {
            const isFocused = node.id === focusedNodeId;
            const isHovered = node.id === hoveredNodeId;
            const isConnected = connectedNodeIds.has(node.id);
            const isRegionMuted = selectedRegion && node.visual.region !== selectedRegion;
            const isKindMuted = filterKind && node.kind !== filterKind;
            const isDimmed = (activeNodeId && !isConnected) || isRegionMuted || isKindMuted;

            const x = node.visual.x;
            const y = node.visual.y;
            const priority = node.visual.priority;

            // Medallion radius based on visual priority
            const radius = priority >= 9 ? 12 : priority >= 7 ? 8.5 : 6;

            // Visual glyph inside medallion
            let glyph = node.visual.glyph || '✦';
            if (node.kind === 'artwork') glyph = '❖';
            else if (node.kind === 'thinker') glyph = '☿';
            else if (node.kind === 'quote') glyph = '❧';

            return (
              <g
                key={node.id}
                data-node-button="true"
                onClick={(e) => {
                  e.stopPropagation();
                  onSelectNode(node.id);
                }}
                onMouseEnter={() => setHoveredNodeId(node.id)}
                onMouseLeave={() => setHoveredNodeId(null)}
                className="cursor-pointer group focus:outline-none"
                tabIndex={0}
                onKeyDown={(e) => {
                  if (e.key === 'Enter' || e.key === ' ') {
                    e.preventDefault();
                    onSelectNode(node.id);
                  }
                }}
                style={{
                  opacity: isDimmed ? 0.18 : 1,
                  transition: 'opacity 0.25s ease-out, transform 0.25s ease-out',
                }}
              >
                {/* Active / Focused Halo Aura */}
                {(isFocused || isHovered) && (
                  <circle
                    cx={x}
                    cy={y}
                    r={radius * 2.8}
                    fill="url(#node-active-halo)"
                    className="animate-pulse"
                  />
                )}

                {/* Outer Brass Ring */}
                <circle
                  cx={x}
                  cy={y}
                  r={radius + 3}
                  fill="none"
                  stroke={isFocused ? 'var(--accent)' : isHovered ? 'var(--accent)' : 'var(--muted)'}
                  strokeWidth={isFocused ? '1.5' : '0.6'}
                  strokeDasharray={node.kind === 'thinker' ? '2 2' : undefined}
                  opacity={isFocused || isHovered ? 1 : 0.4}
                />

                {/* Core Medallion Disc */}
                <circle
                  cx={x}
                  cy={y}
                  r={radius}
                  fill={isFocused ? 'var(--accent)' : isHovered ? 'var(--surface-raised)' : 'var(--surface)'}
                  stroke="var(--accent)"
                  strokeWidth={isFocused ? '1.5' : '1'}
                  className="transition-colors duration-200"
                />

                {/* Celestial Glyph */}
                <text
                  x={x}
                  y={y + (radius <= 6 ? 2.5 : 3.5)}
                  textAnchor="middle"
                  fontSize={radius <= 6 ? '7' : radius <= 8.5 ? '8.5' : '11'}
                  fontFamily="serif"
                  fill={isFocused ? 'var(--bg)' : 'var(--accent)'}
                  className="pointer-events-none select-none font-medium"
                >
                  {glyph}
                </text>

                {/* Semantic Level of Detail (LOD) Label Visibility for pristine Antique Cartography */}
                {(isFocused || isHovered || priority >= 10 || (zoomLevel >= 1.7 && priority >= 8) || zoomLevel >= 2.2) && (
                  <g className="pointer-events-none transition-opacity duration-200">
                    <rect
                      x={x - Math.min(65, Math.max(35, node.label.length * 3.8))}
                      y={y + radius + 5}
                      width={Math.min(130, Math.max(70, node.label.length * 7.6))}
                      height="16"
                      rx="2"
                      fill="var(--surface)"
                      fillOpacity="0.94"
                      stroke={isFocused ? 'var(--accent)' : 'var(--border)'}
                      strokeWidth={isFocused ? '0.8' : '0.4'}
                      strokeOpacity={isFocused ? '0.9' : '0.6'}
                    />
                    <text
                      x={x}
                      y={y + radius + 16}
                      textAnchor="middle"
                      fontFamily="Literata, serif"
                      fontSize="8.5"
                      fill={isFocused ? 'var(--accent)' : 'var(--text)'}
                      className="font-medium select-none"
                    >
                      {node.label.length > 22 ? `${node.label.slice(0, 20)}…` : node.label}
                    </text>
                  </g>
                )}
              </g>
            );
          })}
        </g>
      </svg>

      {/* Floating Hover Cartouche Tooltip */}
      {hoveredNode && !focusedNodeId && (
        <div
          className="absolute pointer-events-none z-30 px-3 py-2 rounded-sm bg-surface/95 border border-accent/60 shadow-xl backdrop-blur-md max-w-xs transition-opacity duration-150 animate-fade-in"
          style={{
            bottom: '24px',
            left: '24px',
          }}
        >
          <div className="flex items-center gap-1.5 text-[10px] font-mono text-accent uppercase tracking-wider mb-0.5">
            <span>✦</span>
            <span>{hoveredNode.kind}</span>
          </div>
          <h4 className="font-serif font-medium text-sm text-text">
            {hoveredNode.label}
          </h4>
          <p className="font-sans text-xs text-muted/90 line-clamp-2 mt-1">
            {hoveredNode.summary}
          </p>
        </div>
      )}
    </div>
  );
};
