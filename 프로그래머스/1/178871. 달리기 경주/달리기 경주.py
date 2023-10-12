def solution(players, callings):
    players_rank = {player:rank for rank, player in enumerate(players)}
    players_name = {rank:player for rank, player in enumerate(players)}
    
    # 선수가 불리면 불린 선수랑 이전 선수 등수 교환
    for call in callings :
        calling_player_rank = players_rank[call] # 불린 선수의 등수
        pre_player_rank = calling_player_rank - 1 # 불린 선수 이전 등수
        calling_player = call # 불린 선수의 이름
        pre_player = players_name[pre_player_rank] # 이전 등수의 이름
        
        players_rank[calling_player] = pre_player_rank # 이전/후 이름의 등수 교체
        players_rank[pre_player] = calling_player_rank 
        players_name[pre_player_rank] = calling_player # 이전/후 등수의 이름 교체
        players_name[calling_player_rank] = pre_player
        
    return sorted(players_rank, key=lambda x:players_rank[x])
