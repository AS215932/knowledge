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
  id TEXT PRIMARY KEY,
  concept_id TEXT NOT NULL,
  subject TEXT NOT NULL,
  predicate TEXT NOT NULL,
  object TEXT NOT NULL,
  authority_tier TEXT NOT NULL,
  source_ref_index INTEGER,
  source_uri TEXT,
  valid_from TEXT,
  valid_to TEXT,
  extracted_at TEXT NOT NULL,
  confidence REAL NOT NULL DEFAULT 1.0,
  freshness_status TEXT NOT NULL DEFAULT 'current',
  review_status TEXT,
  supersedes_json TEXT NOT NULL DEFAULT '[]',
  conflicts_with_json TEXT NOT NULL DEFAULT '[]',
  metadata_json TEXT NOT NULL DEFAULT '{}'
);

CREATE INDEX IF NOT EXISTS idx_claims_subject ON claims(subject);
CREATE INDEX IF NOT EXISTS idx_claims_predicate ON claims(predicate);
CREATE INDEX IF NOT EXISTS idx_claims_object ON claims(object);
CREATE INDEX IF NOT EXISTS idx_claims_authority ON claims(authority_tier);
CREATE INDEX IF NOT EXISTS idx_claims_concept ON claims(concept_id);

CREATE TABLE IF NOT EXISTS retrieval_candidates (
  query_id TEXT NOT NULL,
  concept_id TEXT NOT NULL,
  rank INTEGER NOT NULL,
  score_exact REAL,
  score_graph REAL,
  score_fts REAL,
  score_vector REAL,
  authority_tier TEXT,
  reason TEXT,
  metadata_json TEXT NOT NULL DEFAULT '{}'
);

CREATE TABLE IF NOT EXISTS context_packs (
  id TEXT PRIMARY KEY,
  task_id TEXT,
  role TEXT NOT NULL,
  generated_at TEXT NOT NULL,
  knowledge_snapshot TEXT NOT NULL,
  retrieval_version TEXT NOT NULL,
  policy_version TEXT NOT NULL,
  token_budget INTEGER NOT NULL,
  risk_level TEXT NOT NULL,
  manifest_json TEXT NOT NULL,
  body_json TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS policy_decisions (
  id TEXT PRIMARY KEY,
  requested_at TEXT NOT NULL,
  actor TEXT NOT NULL,
  action TEXT NOT NULL,
  target TEXT,
  environment TEXT,
  risk_level TEXT,
  result TEXT NOT NULL,
  policy_version TEXT NOT NULL,
  reasons_json TEXT NOT NULL DEFAULT '[]',
  constraints_json TEXT NOT NULL DEFAULT '[]',
  input_json TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS eval_cases (
  id TEXT PRIMARY KEY,
  suite TEXT NOT NULL,
  task TEXT NOT NULL,
  role TEXT,
  case_json TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS eval_results (
  run_id TEXT NOT NULL,
  case_id TEXT NOT NULL,
  suite TEXT NOT NULL,
  passed INTEGER NOT NULL,
  score REAL NOT NULL,
  metrics_json TEXT NOT NULL,
  failure_reasons_json TEXT NOT NULL DEFAULT '[]',
  PRIMARY KEY (run_id, case_id)
);

CREATE TABLE IF NOT EXISTS learning_events (
  id TEXT PRIMARY KEY,
  ledger_version TEXT NOT NULL,
  event_type TEXT NOT NULL,
  event_time TEXT NOT NULL,
  producer TEXT NOT NULL,
  subject TEXT NOT NULL,
  summary TEXT NOT NULL,
  status TEXT NOT NULL,
  authority_tier TEXT NOT NULL,
  source_json TEXT NOT NULL DEFAULT '{}',
  data_classes_json TEXT NOT NULL DEFAULT '[]',
  citations_json TEXT NOT NULL DEFAULT '[]',
  context_pack_ids_json TEXT NOT NULL DEFAULT '[]',
  policy_decision_ids_json TEXT NOT NULL DEFAULT '[]',
  eval_case_ids_json TEXT NOT NULL DEFAULT '[]',
  metrics_json TEXT NOT NULL DEFAULT '{}',
  lessons_json TEXT NOT NULL DEFAULT '[]',
  promotion_json TEXT NOT NULL DEFAULT '{}',
  metadata_json TEXT NOT NULL DEFAULT '{}',
  body_json TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_learning_events_type ON learning_events(event_type);
CREATE INDEX IF NOT EXISTS idx_learning_events_producer ON learning_events(producer);
CREATE INDEX IF NOT EXISTS idx_learning_events_subject ON learning_events(subject);
CREATE INDEX IF NOT EXISTS idx_learning_events_status ON learning_events(status);

CREATE TABLE IF NOT EXISTS learning_reviews (
  id TEXT PRIMARY KEY,
  event_id TEXT NOT NULL,
  event_type TEXT NOT NULL,
  decision TEXT NOT NULL,
  promotion_kind TEXT NOT NULL,
  reviewer TEXT NOT NULL,
  reviewed_at TEXT NOT NULL,
  rationale TEXT NOT NULL,
  target_concept_id TEXT,
  target_path TEXT,
  authority_tier_after_promotion TEXT,
  event_hash TEXT NOT NULL,
  validation_errors_json TEXT NOT NULL DEFAULT '[]',
  source_refs_json TEXT NOT NULL DEFAULT '[]',
  body_json TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_learning_reviews_event ON learning_reviews(event_id);
CREATE INDEX IF NOT EXISTS idx_learning_reviews_decision ON learning_reviews(decision);
CREATE INDEX IF NOT EXISTS idx_learning_reviews_target ON learning_reviews(target_concept_id);

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
