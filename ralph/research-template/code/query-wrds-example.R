#!/usr/bin/env Rscript

# How to run: WRDS_USERNAME=<username> WRDS_PASSWORD=<password> Rscript ralph/research-template/code/query-wrds-example.R
# Inputs: WRDS connection settings from environment variables or libpq defaults.
# Outputs: Prints 5 rows from crsp.dsf and exits 0 if the WRDS setup works.

suppressPackageStartupMessages({
  library(DBI)
  library(RPostgres)
})

username <- Sys.getenv("WRDS_USERNAME", unset = Sys.getenv("PGUSER", unset = ""))
password <- Sys.getenv("WRDS_PASSWORD", unset = Sys.getenv("PGPASSWORD", unset = ""))
host <- Sys.getenv("WRDS_HOST", unset = "wrds-pgdata.wharton.upenn.edu")
port <- as.integer(Sys.getenv("WRDS_PORT", unset = "9737"))
dbname <- Sys.getenv("WRDS_DBNAME", unset = "wrds")
sslmode <- Sys.getenv("WRDS_SSLMODE", unset = "require")

if (username == "") {
  stop("Set WRDS_USERNAME (or PGUSER) before running this script.", call. = FALSE)
}

connect_args <- list(
  drv = Postgres(),
  host = host,
  port = port,
  dbname = dbname,
  user = username,
  sslmode = sslmode
)

if (password != "") {
  connect_args$password <- password
}

con <- do.call(dbConnect, connect_args)
on.exit(dbDisconnect(con), add = TRUE)

query <- paste(
  "select *",
  "from crsp.dsf",
  "limit 5"
)

result <- dbGetQuery(con, query)

cat("WRDS query succeeded.\n")
cat(sprintf("Host: %s\n", host))
cat(sprintf("Database: %s\n", dbname))
cat(sprintf("Rows returned: %d\n\n", nrow(result)))
print(result)
