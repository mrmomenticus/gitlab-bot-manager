-- users table
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    id_tg INTEGER UNIQUE NOT NULL,
    username VARCHAR NOT NULL,
    token VARCHAR NOT NULL
);

-- projects table
CREATE TABLE IF NOT EXISTS projects (
    id SERIAL PRIMARY KEY,
    id_git INTEGER UNIQUE NOT NULL,
    name VARCHAR NOT NULL,
    description VARCHAR NOT NULL,
    date_create DATE NOT NULL,
    notification BOOLEAN NOT NULL,
    processing BOOLEAN NOT NULL
);

-- merges table
CREATE TABLE IF NOT EXISTS merges (
    id SERIAL PRIMARY KEY,
    id_merge INTEGER UNIQUE NOT NULL,
    project_id INTEGER NOT NULL REFERENCES projects(id) ON DELETE CASCADE,
    title VARCHAR NOT NULL,
    description VARCHAR NOT NULL,
    state VARCHAR NOT NULL,
    created_date DATE NOT NULL,
    updated_date DATE NOT NULL,
    conflict BOOLEAN NOT NULL,
    source_branch VARCHAR NOT NULL,
    target_branch VARCHAR NOT NULL,
    notification BOOLEAN NOT NULL,
    author_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    assignee_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    is_assigned BOOLEAN NOT NULL,
    is_reviewed BOOLEAN NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_merges_project_id ON merges(project_id);
CREATE INDEX IF NOT EXISTS idx_merges_author_id ON merges(author_id);
CREATE INDEX IF NOT EXISTS idx_merges_assignee_id ON merges(assignee_id);