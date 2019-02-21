# mi: the simplest database migration utility
    
## Description
    
    $ mi help 
    mi utility.

    Helps manage migrations in raw sql.
    
    Usage:
      mi init [--db=db]
      mi check
      mi new [<name>]
      mi apply [<names>...]
      mi -h | --help
      mi help
    
    Subcommands:
      mi init          Create .mi.json
      mi check         Check for unapplied migrations
      mi new           Create empty migration
      mi apply         Apply migration(s)

## Install

    pip install -e .

Run init:

    $ mi init --db postgresql://postgres:postgres@localhost:5432/mydb
    {
        "database_url": "postgresql://postgres:postgres@localhost:5432/mydb",
        "migrations_dir": "migrations"
    }
    
Besides the `--db` option, you can set `$DATABASE_URL` environment variable.



## Usage

    $ mi check
    All migrations are applied.

    $ mi new alter_table
    0004_alter_table.sql is generated. Please fill it with meaning.

    $ mi apply
    Applied: 0003.sql
    Applied: 0004_alter_table.sql



## Missing features

- Migrations dependencies
  
  Migrations are executed in the order of their names. Timestamp is also preserver though
  
- Only postresql is supported

