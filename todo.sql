CREATE TABLE IF NOT EXISTS todos (
    sno INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    desc TEXT NOT NULL,
    date_created DATETIME,
    status TEXT DEFAULT 'Pending'
);