def main():
    with open("input.txt") as f:
        reports = [list(map(int, line.split())) for line in f]

    safe_reports_count = 0

    for report in reports:
        if len(report) <= 1:
            safe_reports_count += 1
            continue
        
        safe = True

        if report[0] < report[1]:
            increasing = True
        elif report[0] > report[1]:
            increasing = False
        
        for i in range(len(report) - 1):
            a = report[i]
            b = report[i + 1]

            if not (3 >= abs(a - b) >= 1):
                safe = False

            if increasing and a >= b:
                safe = False
            elif not increasing and a <= b:
                safe = False
                
        if safe:
            safe_reports_count += 1
    
    print(safe_reports_count)

if __name__ == "__main__":
    main()