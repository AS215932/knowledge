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
