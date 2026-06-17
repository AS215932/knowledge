CREATE TABLE IF NOT EXISTS concepts (
  id TEXT PRIMARY KEY,
  path TEXT NOT NULL,
  type TEXT NOT NULL,
  title TEXT,
  description TEXT,
  resource TEXT,
  tags_json TEXT NOT NULL DEFAULT '[]',
  truth_owner TEXT,
  authority TEXT,
  confidence TEXT,
  dispute_policy TEXT,
  last_verified_at TEXT,
  review_status TEXT,
  quality_score REAL,
  observed_at TEXT,
  expires_at TEXT,
  enrichment_json TEXT,
  body TEXT NOT NULL DEFAULT ''
);

CREATE TABLE IF NOT EXISTS source_refs (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  concept_id TEXT NOT NULL REFERENCES concepts(id) ON DELETE CASCADE,
  repo TEXT,
  path TEXT,
  commit_sha TEXT,
  lines TEXT,
  url TEXT
);

CREATE TABLE IF NOT EXISTS edges (
  source TEXT NOT NULL,
  target TEXT NOT NULL,
  edge_type TEXT NOT NULL,
  origin TEXT NOT NULL,
  confidence TEXT NOT NULL,
  PRIMARY KEY (source, target, edge_type)
);

CREATE TABLE IF NOT EXISTS github_items (
  id TEXT PRIMARY KEY,
  repo TEXT NOT NULL,
  item_type TEXT NOT NULL,
  number INTEGER,
  title TEXT,
  state TEXT,
  url TEXT,
  updated_at TEXT,
  payload_json TEXT NOT NULL DEFAULT '{}'
);

CREATE TABLE IF NOT EXISTS quality_findings (
  concept_id TEXT NOT NULL,
  severity TEXT NOT NULL,
  code TEXT NOT NULL,
  message TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS observations (
  concept_id TEXT NOT NULL,
  observed_at TEXT,
  expires_at TEXT,
  source TEXT,
  status TEXT,
  payload_json TEXT NOT NULL DEFAULT '{}'
);

CREATE TABLE IF NOT EXISTS claims (
  concept_id TEXT NOT NULL,
  claim_text TEXT NOT NULL,
  source_ref_index INTEGER,
  confidence TEXT
);

CREATE TABLE IF NOT EXISTS enrichment_runs (
  run_id TEXT PRIMARY KEY,
  concept_id TEXT,
  provider TEXT,
  model TEXT,
  prompt_version TEXT,
  input_hash TEXT,
  output_hash TEXT,
  created_at TEXT
);

CREATE TABLE IF NOT EXISTS runs (
  run_id TEXT PRIMARY KEY,
  started_at TEXT NOT NULL,
  completed_at TEXT,
  source_shas_json TEXT NOT NULL DEFAULT '{}',
  concept_count INTEGER NOT NULL DEFAULT 0,
  edge_count INTEGER NOT NULL DEFAULT 0
);

CREATE VIRTUAL TABLE IF NOT EXISTS concept_fts USING fts5(
  id UNINDEXED,
  title,
  description,
  body,
  tags
);
