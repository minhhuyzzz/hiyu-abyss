// website/src/components/atlas/AtlasMap.tsx
// Antique Celestial Atlas × Renaissance Portolan Cartography Plate
import React, { useRef, useState, useEffect, useMemo } from 'react';
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
  userThreadNodeIds?: string[];
  onClearThread?: () => void;
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
  userThreadNodeIds = [],
  onClearThread,
}) => {
  const containerRef = useRef<HTMLDivElement>(null);
  const [isDragging, setIsDragging] = useState(false);
  const [dragStart, setDragStart] = useState({ x: 0, y: 0 });
  const [hoveredNodeId, setHoveredNodeId] = useState<string | null>(null);

  // Map node lookup by ID
  const nodeMap = useMemo(() => new Map(nodes.map((n) => [n.id, n])), [nodes]);

  // Identify connected node IDs when a node is hovered or focused
  const activeNodeId = hoveredNodeId || focusedNodeId;
  const connectedNodeIds = useMemo(() => {
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
    const newZoom = Math.max(0.6, Math.min(3.2, zoomLevel * zoomFactor));
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
      const newZoom = Math.max(0.6, Math.min(3.2, zoomLevel * factor));
      onZoomChange(newZoom);
      touchStartRef.current.dist = dist;
    }
  };

  const handleTouchEnd = () => {
    setIsDragging(false);
    touchStartRef.current = null;
  };

  // Portolan Navigation Rhumb Lines generation (Inspired by authentic 16th-century nautical charts)
  const rhumbRays = useMemo(() => {
    const centers = [
      { x: 500, y: 120 },
      { x: 768, y: 232 },
      { x: 880, y: 500 },
      { x: 768, y: 768 },
      { x: 500, y: 880 },
      { x: 232, y: 768 },
      { x: 120, y: 500 },
      { x: 232, y: 232 },
    ];
    const lines: Array<{ x1: number; y1: number; x2: number; y2: number }> = [];
    for (let i = 0; i < centers.length; i++) {
      for (let j = i + 1; j < centers.length; j++) {
        lines.push({
          x1: centers[i].x,
          y1: centers[i].y,
          x2: centers[j].x,
          y2: centers[j].y,
        });
      }
      // Line to center
      lines.push({
        x1: centers[i].x,
        y1: centers[i].y,
        x2: 500,
        y2: 500,
      });
    }
    return lines;
  }, []);

  // Build user travel thread path (The Thread)
  const threadPath = useMemo(() => {
    if (!userThreadNodeIds || userThreadNodeIds.length < 2) return '';
    const points = userThreadNodeIds
      .map((id) => nodeMap.get(id))
      .filter(Boolean)
      .map((n) => ({ x: n!.visual.x, y: n!.visual.y }));

    if (points.length < 2) return '';
    let d = `M ${points[0].x} ${points[0].y}`;
    for (let i = 1; i < points.length; i++) {
      const prev = points[i - 1];
      const curr = points[i];
      // Subtle bezier curve for organic ink feel
      const midX = (prev.x + curr.x) / 2;
      const midY = (prev.y + curr.y) / 2;
      const dx = curr.x - prev.x;
      const dy = curr.y - prev.y;
      const curveOffset = Math.min(20, Math.hypot(dx, dy) * 0.1);
      const cpX = midX - (dy / (Math.hypot(dx, dy) || 1)) * curveOffset;
      const cpY = midY + (dx / (Math.hypot(dx, dy) || 1)) * curveOffset;
      d += ` Q ${cpX} ${cpY} ${curr.x} ${curr.y}`;
    }
    return d;
  }, [userThreadNodeIds, nodeMap]);

  // Latin Realm Banners
  const getLatinRegionTitle = (id: string) => {
    switch (id) {
      case 'region-human-condition':
        return 'I · NATURA HUMANA';
      case 'region-ego-and-illusion':
        return 'II · EGO ET ILLUSIO';
      case 'region-freedom-and-order':
        return 'III · LIBERTAS ET ORDO';
      case 'region-solitude-and-communion':
        return 'IV · SOLITUDO ET COMMVNIO';
      case 'region-power-and-machination':
        return 'V · POTENTIA ET FRAUS';
      case 'region-suffering-and-purpose':
        return 'VI · DOLOR ET RATIO';
      case 'region-masks-and-authenticity':
        return 'VII · PERSONA ET VMBRA';
      case 'region-aesthetics-and-worldview':
        return 'VIII · AESTHETICA VNIVERSALIS';
      default:
        return 'TERRA COGNITA';
    }
  };

  const hoveredNode = hoveredNodeId ? nodeMap.get(hoveredNodeId) : null;

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
      {/* 1. Ornate Windrose / Compass Rose in Corner */}
      <div className="absolute top-4 left-4 pointer-events-none z-10 opacity-60 hidden sm:block">
        <svg width="90" height="90" viewBox="0 0 100 100" className="text-accent stroke-current fill-none">
          {/* Compass Rings */}
          <circle cx="50" cy="50" r="44" strokeWidth="1" />
          <circle cx="50" cy="50" r="40" strokeWidth="0.5" strokeDasharray="1.5 2" />
          <circle cx="50" cy="50" r="34" strokeWidth="0.5" />
          {/* 8 Principal Wind Pointers */}
          <path d="M50 6 L53 45 L50 50 L47 45 Z" fill="currentColor" opacity="0.9" />
          <path d="M50 94 L53 55 L50 50 L47 55 Z" fill="currentColor" opacity="0.4" />
          <path d="M6 50 L45 47 L50 50 L45 53 Z" fill="currentColor" opacity="0.4" />
          <path d="M94 50 L55 47 L50 50 L55 53 Z" fill="currentColor" opacity="0.4" />
          <path d="M19 19 L46 46 L50 50 L44 47 Z" fill="currentColor" opacity="0.3" />
          <path d="M81 19 L54 46 L50 50 L56 47 Z" fill="currentColor" opacity="0.3" />
          <path d="M19 81 L46 54 L50 50 L47 56 Z" fill="currentColor" opacity="0.3" />
          <path d="M81 81 L54 54 L50 50 L53 56 Z" fill="currentColor" opacity="0.3" />
          {/* Cardinal Directions */}
          <text x="50" y="4" textAnchor="middle" fontSize="6.5" fontFamily="Cinzel, Cormorant Garamond, serif" fontWeight="bold" fill="currentColor">N · SEPTENTRIO</text>
          <text x="97" y="52" textAnchor="middle" fontSize="6.5" fontFamily="Cinzel, Cormorant Garamond, serif" fontWeight="bold" fill="currentColor">E</text>
          <text x="50" y="100" textAnchor="middle" fontSize="6.5" fontFamily="Cinzel, Cormorant Garamond, serif" fontWeight="bold" fill="currentColor">S · MERIDIES</text>
          <text x="3" y="52" textAnchor="middle" fontSize="6.5" fontFamily="Cinzel, Cormorant Garamond, serif" fontWeight="bold" fill="currentColor">W</text>
        </svg>
      </div>

      {/* 2. Floating User Thread Indicator (The Thread Breadcrumb) */}
      {userThreadNodeIds && userThreadNodeIds.length >= 2 && (
        <div className="absolute bottom-5 left-5 z-20 px-3.5 py-2.5 rounded-sm bg-surface/95 border border-accent/40 shadow-xl backdrop-blur-md flex items-center gap-3 animate-fade-in">
          <div className="w-2.5 h-2.5 rounded-full bg-[#B47862] animate-ping" />
          <div>
            <div className="text-[10px] font-mono uppercase tracking-widest text-accent">
              Sợi Chỉ Tư Tưởng Của Bạn
            </div>
            <div className="text-xs font-serif text-text font-medium">
              Đã khắc {userThreadNodeIds.length} chặng hành trình
            </div>
          </div>
          {onClearThread && (
            <button
              onClick={onClearThread}
              className="ml-2 text-[10px] font-mono text-muted hover:text-text px-2 py-1 rounded bg-bg border border-border transition-colors"
              title="Xóa dấu vết hành trình"
            >
              Làm mới
            </button>
          )}
        </div>
      )}

      {/* 3. Main SVG Celestial Cartography Plate */}
      <svg
        viewBox="0 0 1000 1000"
        className="w-full h-full will-change-transform"
        style={{
          transform: `translate(${panOffset.x}px, ${panOffset.y}px) scale(${zoomLevel})`,
          transformOrigin: '50% 50%',
          transition: isDragging ? 'none' : 'transform 0.45s cubic-bezier(0.16, 1, 0.3, 1)',
        }}
      >
        <defs>
          {/* Subtle Celestial Radial Gradients */}
          <radialGradient id="celestial-plate-glow" cx="50%" cy="50%" r="50%">
            <stop offset="0%" stopColor="var(--accent)" stopOpacity="0.08" />
            <stop offset="65%" stopColor="var(--accent)" stopOpacity="0.02" />
            <stop offset="100%" stopColor="transparent" stopOpacity="0" />
          </radialGradient>

          <radialGradient id="node-active-halo" cx="50%" cy="50%" r="50%">
            <stop offset="0%" stopColor="var(--accent)" stopOpacity="0.5" />
            <stop offset="100%" stopColor="var(--accent)" stopOpacity="0" />
          </radialGradient>

          {/* Region Terrains */}
          {regions.map((r) => (
            <radialGradient key={r.id} id={`halo-${r.id}`} cx="50%" cy="50%" r="50%">
              <stop offset="0%" stopColor={r.colorToken} stopOpacity="0.14" />
              <stop offset="70%" stopColor={r.colorToken} stopOpacity="0.03" />
              <stop offset="100%" stopColor="transparent" stopOpacity="0" />
            </radialGradient>
          ))}
        </defs>

        {/* 1. Background Plate */}
        <rect width="1000" height="1000" fill="url(#celestial-plate-glow)" />

        {/* 2. Authentic Portolan Rhumb Lines (Image 4) */}
        <g className="pointer-events-none opacity-25">
          {rhumbRays.map((ray, idx) => (
            <line
              key={idx}
              x1={ray.x1}
              y1={ray.y1}
              x2={ray.x2}
              y2={ray.y2}
              stroke={idx % 2 === 0 ? '#B47862' : '#C29A77'}
              strokeWidth="0.4"
              strokeDasharray={idx % 3 === 0 ? '1 3' : undefined}
            />
          ))}
        </g>

        {/* 3. Celestial Astrolabe Graduations & Great Rings (Image 1) */}
        <g className="text-accent/25 stroke-current fill-none pointer-events-none">
          {/* Outer Graduated Frame */}
          <circle cx="500" cy="500" r="488" strokeWidth="2.5" />
          <circle cx="500" cy="500" r="480" strokeWidth="0.5" strokeDasharray="1.5 2" />
          <circle cx="500" cy="500" r="460" strokeWidth="1" />
          
          {/* Concentric Coordinate Rings */}
          <circle cx="500" cy="500" r="330" strokeWidth="0.75" strokeDasharray="4 4" />
          <circle cx="500" cy="500" r="190" strokeWidth="0.75" strokeDasharray="3 3" />
          <circle cx="500" cy="500" r="60" strokeWidth="0.5" strokeDasharray="2 2" />

          {/* Equinoctial Colure & Solstitial Meridian */}
          <line x1="500" y1="12" x2="500" y2="988" strokeWidth="0.6" strokeDasharray="4 4" />
          <line x1="12" y1="500" x2="988" y2="500" strokeWidth="0.6" strokeDasharray="4 4" />

          {/* Antique Degree Tick Marks on Rim */}
          {Array.from({ length: 72 }).map((_, i) => {
            const angle = (i * 5 * Math.PI) / 180;
            const r1 = i % 6 === 0 ? 472 : 477;
            const r2 = 480;
            return (
              <line
                key={i}
                x1={500 + r1 * Math.cos(angle)}
                y1={500 + r1 * Math.sin(angle)}
                x2={500 + r2 * Math.cos(angle)}
                y2={500 + r2 * Math.sin(angle)}
                strokeWidth={i % 6 === 0 ? '1' : '0.5'}
              />
            );
          })}

          {/* Roman Astronomical Inscriptions */}
          <text x="500" y="32" textAnchor="middle" fontSize="9.5" fontFamily="Cormorant Garamond, serif" letterSpacing="2.5" fill="currentColor">
            XII · POLUS ARCTICUS · ZENITH
          </text>
          <text x="500" y="980" textAnchor="middle" fontSize="9.5" fontFamily="Cormorant Garamond, serif" letterSpacing="2.5" fill="currentColor">
            VI · POLUS ANTARCTICUS · NADIR
          </text>
          <text x="965" y="504" textAnchor="end" fontSize="9.5" fontFamily="Cormorant Garamond, serif" letterSpacing="2" fill="currentColor">
            III · ORIENS
          </text>
          <text x="35" y="504" textAnchor="start" fontSize="9.5" fontFamily="Cormorant Garamond, serif" letterSpacing="2" fill="currentColor">
            IX · OCCIDENS
          </text>

          {/* Monumental Renaissance Cartouche Motto (Image 1 & 2) */}
          <g className="opacity-80 pointer-events-none select-none">
            <text
              x="500"
              y="56"
              textAnchor="middle"
              fontFamily="Cinzel, Cormorant Garamond, serif"
              fontSize="10.5"
              letterSpacing="3"
              fill="var(--accent)"
              className="font-semibold uppercase"
            >
              ✦ PLANISPHAERIUM MENTIS · TABULA TOTIUS MUNDI INTERIORIS ✦
            </text>
            <text
              x="500"
              y="952"
              textAnchor="middle"
              fontFamily="Cinzel, Cormorant Garamond, serif"
              fontSize="8.5"
              letterSpacing="2.5"
              fill="var(--muted)"
              className="uppercase opacity-70"
            >
              HIYU ABYSS · CARTOGRAPHIA PHILOSOPHICA & PSYCHOLOGICA · ANNO MMXXVI
            </text>
          </g>
        </g>

        {/* 4. 8 Curated Regions: Cartographic Terrains & Latin Ribbons (The Entrance) */}
        <g className="pointer-events-none">
          {regions.map((region) => {
            const isRegionSelected = !selectedRegion || selectedRegion === region.id;
            return (
              <g
                key={region.id}
                className="transition-opacity duration-300"
                style={{ opacity: isRegionSelected ? 1 : 0.2 }}
              >
                {/* Realm Terrain Halo */}
                <circle
                  cx={region.centerCoordinates.x}
                  cy={region.centerCoordinates.y}
                  r="175"
                  fill={`url(#halo-${region.id})`}
                />
                {/* Engraved Realm Frontier Boundary */}
                <circle
                  cx={region.centerCoordinates.x}
                  cy={region.centerCoordinates.y}
                  r="175"
                  stroke={region.colorToken}
                  strokeWidth="0.75"
                  strokeDasharray="4 8"
                  opacity="0.3"
                  fill="none"
                />

                {/* Latin Cartouche Ribbon */}
                <g className="transition-transform duration-300">
                  <rect
                    x={region.centerCoordinates.x - 90}
                    y={region.centerCoordinates.y - 134}
                    width="180"
                    height="28"
                    rx="2"
                    fill="var(--surface)"
                    fillOpacity="0.85"
                    stroke={region.colorToken}
                    strokeWidth="0.6"
                    strokeOpacity="0.5"
                  />
                  <text
                    x={region.centerCoordinates.x}
                    y={region.centerCoordinates.y - 120}
                    textAnchor="middle"
                    fontFamily="Cinzel, Cormorant Garamond, serif"
                    fontSize="9"
                    letterSpacing="1.8"
                    fill={region.colorToken}
                    className="font-semibold uppercase select-none"
                  >
                    {region.astronomyGlyph} {getLatinRegionTitle(region.id)}
                  </text>
                  <text
                    x={region.centerCoordinates.x}
                    y={region.centerCoordinates.y - 110}
                    textAnchor="middle"
                    fontFamily="Literata, serif"
                    fontSize="8.5"
                    fontStyle="italic"
                    fill="var(--text)"
                    className="select-none opacity-80"
                  >
                    {region.label}
                  </text>
                </g>
              </g>
            );
          })}
        </g>

        {/* 5. Constellation Ink Edges (The Unfolding) */}
        <g>
          {edges.map((edge) => {
            const source = nodeMap.get(edge.from);
            const target = nodeMap.get(edge.to);
            if (!source || !target) return null;

            const isConnectedToActive =
              activeNodeId && (edge.from === activeNodeId || edge.to === activeNodeId);
            const isFaded = activeNodeId && !isConnectedToActive;

            // Stroke styling based on relation
            let strokeColor = 'var(--accent)';
            let strokeDash = undefined;
            if (edge.relation === 'contrasts_with') {
              strokeColor = 'var(--oxide)'; // Oxide red
              strokeDash = '4 3';
            } else if (edge.relation === 'influenced_by') {
              strokeColor = 'var(--patina)'; // Patina jade
              strokeDash = '2 2';
            }

            const strokeOpacity = isConnectedToActive ? 0.95 : isFaded ? 0.04 : 0.18;
            const strokeWidth = isConnectedToActive ? 2.0 : 0.75;

            // Curved Quadratic Bezier Calculation
            const midX = (source.visual.x + target.visual.x) / 2;
            const midY = (source.visual.y + target.visual.y) / 2;
            const dx = target.visual.x - source.visual.x;
            const dy = target.visual.y - source.visual.y;
            const dist = Math.hypot(dx, dy) || 1;
            const offsetDist = Math.min(26, dist * 0.08);
            const perpX = midX - (dy / dist) * offsetDist;
            const perpY = midY + (dx / dist) * offsetDist;

            const pathD = `M ${source.visual.x} ${source.visual.y} Q ${perpX} ${perpY} ${target.visual.x} ${target.visual.y}`;

            return (
              <g key={edge.id} className="transition-all duration-300">
                <path
                  d={pathD}
                  fill="none"
                  stroke={strokeColor}
                  strokeWidth={strokeWidth}
                  strokeDasharray={strokeDash}
                  strokeOpacity={strokeOpacity}
                />
                {/* Active Directional Gold Ink Bead */}
                {isConnectedToActive && (
                  <circle
                    cx={perpX}
                    cy={perpY}
                    r="2.5"
                    fill={strokeColor}
                    opacity="0.9"
                  />
                )}
              </g>
            );
          })}
        </g>

        {/* 6. The Thread — Sợi Chỉ Tư Tưởng Cá Nhân (Image 4 & Pillar 04) */}
        {threadPath && (
          <g className="pointer-events-none">
            {/* Glowing Vermilion Thread Background Aura */}
            <path
              d={threadPath}
              fill="none"
              stroke="#B47862"
              strokeWidth="4"
              strokeOpacity="0.25"
              strokeLinecap="round"
            />
            {/* Crisp Ink Core Thread */}
            <path
              d={threadPath}
              fill="none"
              stroke="#B47862"
              strokeWidth="1.6"
              strokeDasharray="4 2"
              strokeOpacity="0.9"
              strokeLinecap="round"
            />
          </g>
        )}

        {/* 7. Nodes — Celestial Medallions (The Unfolding & LOD) */}
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

            // In Pillar 01: At zoom 1.0 (The Entrance), nodes are delicate stellar stars, avoiding hundreds of raw dots
            const isOverviewMode = zoomLevel < 1.3 && !activeNodeId;
            const radius = isOverviewMode
              ? priority >= 10
                ? 8
                : priority >= 8
                ? 5
                : 3.5
              : priority >= 9
              ? 12
              : priority >= 7
              ? 8.5
              : 6;

            // Glyphs
            let glyph = node.visual.glyph || '✦';
            if (node.kind === 'artwork') glyph = '❖';
            else if (node.kind === 'thinker') glyph = '☿';
            else if (node.kind === 'quote') glyph = '❧';

            // Check if node is part of the user's thread
            const threadIndex = userThreadNodeIds ? userThreadNodeIds.indexOf(node.id) : -1;

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
                  opacity: isDimmed ? 0.16 : 1,
                  transition: 'opacity 0.25s ease-out',
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
                  opacity={isFocused || isHovered ? 1 : 0.35}
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

                {/* Celestial Glyph (visible when expanded) */}
                {(!isOverviewMode || priority >= 8) && (
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
                )}

                {/* Step badge if visited on User Thread */}
                {threadIndex >= 0 && (
                  <g className="pointer-events-none">
                    <circle
                      cx={x + radius + 1}
                      cy={y - radius - 1}
                      r="6"
                      fill="#B47862"
                      stroke="var(--bg)"
                      strokeWidth="1"
                    />
                    <text
                      x={x + radius + 1}
                      y={y - radius + 2}
                      textAnchor="middle"
                      fontSize="6.5"
                      fontFamily="mono"
                      fontWeight="bold"
                      fill="#FFFFFF"
                    >
                      {threadIndex + 1}
                    </text>
                  </g>
                )}

                {/* Semantic Level of Detail (LOD) Label Visibility */}
                {(isFocused || isHovered || (zoomLevel >= 1.7 && priority >= 8) || zoomLevel >= 2.2) && (
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
            <span>{hoveredNode.kind.toUpperCase()}</span>
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
