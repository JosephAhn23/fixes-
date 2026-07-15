There is an Apache-style access log at /app/access.log. Parse it and write a JSON summary report to /app/report.json.

The report must be a single JSON object with exactly these keys:
- total_requests: integer count of non-empty log lines
- unique_ips: integer count of distinct client IP addresses (first field of each line)
- top_path: the request path that appears most often (the path from the request line, e.g. /index.html); ties may be broken arbitrarily among equally frequent paths

Success criteria:
1. /app/report.json exists after you finish.
2. /app/report.json is valid JSON and is a single object containing the keys total_requests, unique_ips, and top_path.
3. total_requests equals the number of non-empty lines in /app/access.log.
4. unique_ips equals the number of distinct client IP addresses in /app/access.log.
5. top_path is the most frequently requested path in /app/access.log.
