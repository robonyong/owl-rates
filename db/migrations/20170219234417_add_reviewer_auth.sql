-- migrate:up
alter table reviewer add column password_hash varchar(128);
alter table reviewer add column is_active boolean;

-- migrate:down
alter table reviewer drop column if exists password_hash;
alter table reviewer drop column if exists is_active;
