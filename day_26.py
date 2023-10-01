# Enter your code here. Read input from STDIN. Print output to STDOUT
return_date,return_month,return_year = [int(e) for e in input().strip().split(' ')]
due_date,due_month,due_year = [int(e) for e in input().strip().split(' ')]

if return_year>due_year:
    print(10000)
    
elif return_year==due_year and return_month>due_month:
    print(500*(return_month-due_month))
 
elif return_year==due_year and return_month==due_month and return_date>due_date:
    print(15*(return_date-due_date))
    
else:
    print(0)




