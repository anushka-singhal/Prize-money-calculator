def calculate_prize(X, results):
    carlsen_wins = results.count('C')
    chef_wins = results.count('N')
    draws = results.count('D')

    total_points_carlsen = 2 * carlsen_wins + draws
    total_points_chef = 2 * chef_wins + draws

    if total_points_carlsen > total_points_chef:
        return 60 * X
    elif total_points_carlsen < total_points_chef:
        return 40 * X
    else:  
        return 55 * X

T = int(input())

for _ in range(T):
    X = int(input())  
    results = input().strip() 
    
    print(calculate_prize(X, results))
