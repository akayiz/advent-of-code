def is_report_safe(report: list[int]) -> list[bool, int]:
    if len(report) <= 1:
        return [True, None]

    if report[0] < report[1]:
        increasing = True
    else:
        increasing = False
    
    for i in range(len(report) - 1):
        a = report[i]
        b = report[i + 1]

        if not (3 >= abs(a - b) >= 1):
            return [False, i]

        if increasing and a >= b:
            return [False, i]
        elif not increasing and a <= b:
            return [False, i]
    
    return [True, None]

def main():
    with open("input.txt") as f:
        reports = [list(map(int, line.split())) for line in f]

    safe_reports_count = 0

    for report in reports:
        result = is_report_safe(report)
        safe = result[0]
        idx = result[1]
        if idx:
            result = is_report_safe(report[:idx] + report[idx+1:])
            safe |= result[0]
            result = is_report_safe(report[:idx+1] + report[idx+2:])
            safe |= result[0]
        result = is_report_safe(report[1:])
        safe |= result[0]
        result = is_report_safe(report[:1] + report[2:])
        safe |= result[0]
                
        if safe:
            safe_reports_count += 1
    
    print(safe_reports_count)

if __name__ == "__main__":
    main()