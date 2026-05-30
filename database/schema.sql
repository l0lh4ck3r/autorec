CREATE TABLE IF NOT EXISTS scans (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    target TEXT,
    profile TEXT,
    status TEXT,
    started_at TEXT,
    completed_at TEXT
);

CREATE TABLE IF NOT EXISTS hosts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    scan_id INTEGER,
    hostname TEXT,
    ip TEXT
);

CREATE TABLE IF NOT EXISTS urls (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    host_id INTEGER,
    url TEXT,
    status_code INTEGER
);

CREATE TABLE IF NOT EXISTS findings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    severity TEXT,
    score INTEGER,
    title TEXT,
    evidence TEXT,
    created_at TEXT
);

CREATE TABLE IF NOT EXISTS technologies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    host TEXT,
    technology TEXT
);

CREATE TABLE IF NOT EXISTS javascript_files (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    url TEXT
);

CREATE TABLE IF NOT EXISTS parameters (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    url TEXT,
    parameter TEXT
);

CREATE TABLE IF NOT EXISTS screenshots (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    host TEXT,
    image_path TEXT
);

CREATE TABLE IF NOT EXISTS scan_state (
    scan_id INTEGER PRIMARY KEY,
    state_json TEXT
);
CREATE TABLE IF NOT EXISTS asset_inventory (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    scan_id INTEGER,
    asset_type TEXT,
    asset_value TEXT,
    first_seen TEXT,
    last_seen TEXT
);

CREATE TABLE IF NOT EXISTS technologies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    host TEXT,
    technology TEXT
);
CREATE TABLE IF NOT EXISTS urls (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    host TEXT,
    url TEXT,
    status_code INTEGER
);
CREATE TABLE IF NOT EXISTS url_inventory (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    scan_id INTEGER,
    url TEXT,
    source TEXT,
    discovered_at TEXT
);
CREATE TABLE IF NOT EXISTS technologies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    scan_id INTEGER,
    host TEXT,
    technology TEXT
);
CREATE TABLE IF NOT EXISTS screenshots (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    scan_id INTEGER,
    host TEXT,
    image_path TEXT,
    created_at TEXT
);