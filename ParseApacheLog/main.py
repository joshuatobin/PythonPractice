

logs=['127.0.0.1 - - [12/Dec/2022:11:43:59 +0000] "GET /index.html HTTP/1.1" 200 1024',
'127.0.0.1 - - [12/Dec/2022:11:44:00 +0000] "POST /api/data HTTP/1.1" 500 2048',
'127.0.0.1 - - [12/Dec/2022:11:44:01 +0000] "GET /about.html HTTP/1.1" 404 512',
'127.0.0.1 - - [12/Dec/2022:11:44:02 +0000] "GET /contact.html HTTP/1.1" 200 1024',
'127.0.0.1 - - [12/Dec/2022:11:44:03 +0000] "POST /api/data HTTP/1.1" 500 2048']


def main():
    """
    Parse the file line by line.
    Extract the status codes (the number following the HTTP request and preceding the response size).
    Count the occurrences of each status code.
    Output the status codes sorted by frequency (highest to lowest). If two status codes have the same count, sort them numerically.
    """
    status_codes = {}
    for l in logs:
        code = l.split(" ")[8]
        if code in status_codes:
            status_codes[code] += 1
        else:
            status_codes[code] = 1

    print(f"Status Codes: {status_codes}")
    
    # If you need to maintain the original order (since sets are unordered), you can use a dictionary with dictionary keys as the unique values:
    ordered = list(dict.fromkeys(status_codes))
    
    print(ordered)
    
    sorted_items = sorted(status_codes.items(), key=lambda item: item[1], reverse=True)
    
    print(sorted_items)

if __name__ == "__main__":
    main()
