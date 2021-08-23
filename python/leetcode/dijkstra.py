G = {
  1: {2:7, 3:9, 6:14},
  2: {1:7, 3:10, 4:15},
  3: {4:11, 6:2, 1:9, 2:10},
  6: {1:14, 5:9, 3:2},
  5: {6:9, 4:6},
  4: {5:6, 3:11, 2:15}
}


print('\n  Граф G')
for i in G:
    print(i, ':', G[i])

N = len(G) 

tops = [] 
tops_to_visit = {} 
track_shortest_way = {} 
current_top = None 
end_top = None 

def dijkstra(current_top, tops_to_visit, visited_tops, track_shortest_way, end_top):
    print('\n  Обходим всех соседей текущей вершины')
    for x in G[current_top]: 
        xm = tops_to_visit[current_top] + G[current_top][x] 
                            
        if not x in tops_to_visit:
            tops_to_visit[x] = xm 
            track_shortest_way[x] = current_top
        elif not x in visited_tops: 
            if tops_to_visit[x] > xm:
                tops_to_visit[x] = xm 
                track_shortest_way[x] = current_top 
            
        print('текущей вершины v =', current_top, ' сосед x =', x, 'c меткой xm =', xm)
    
    print('p =', tops_to_visit)
    
    print('\n  Добавляем текущую вершину в список посещенных')
    visited_tops.append(current_top)            
    print('t =', visited_tops) 
    
    if N <= len(visited_tops): 
        print('\nВсё!\nВершины и их метки =', tops_to_visit)
        print('Словарь для отслеживания пути =', track_shortest_way)
        
        s = [] 
        s.insert(0, end_top) 
        
        while True:
            if track_shortest_way[end_top] == -1: 
                print('Кратчайший путь от начальной до конечной вершины =', s)
                break
            end_top = track_shortest_way[end_top]
            s.insert(0, end_top) 
                 
        return  s         
    
    print('\n  Находим вершину с минимальной меткой за исключением тех, что уже в t')
    for d in tops_to_visit:
        if d not in visited_tops:
            dm = tops_to_visit[d]
            break 
    
    for y in tops_to_visit:
        if tops_to_visit[y] < dm and not y in visited_tops: 
            dm = tops_to_visit[y] 
            d = y 
            print('Вершина y =', y, 'с меткой dm =', dm)
    
            print('Вершина d =', d, 'имеет минимальную метку dm =', dm, \
                '\nтеперь текущей вершиной v будет вершина d')
            current_top = d 
    
    print('\n  Рекурсивно вызываем функцию Дейкстры с параметрами v, p, t, b, e')
    dijkstra(current_top, tops_to_visit, visited_tops, track_shortest_way, end_top)
  
def start_v(start, end):
    current_top = start
    end_top = end
    tops_to_visit[current_top] = 0
    track_shortest_way[current_top] = -1
    print('\n  Начальная текущая вершина v =', current_top)
    return current_top, tops_to_visit, track_shortest_way, end_top
    
current_top, tops_to_visit, track_shortest_way, end_top = start_v(1, 5)  
dijkstra(current_top, tops_to_visit, tops, track_shortest_way, end_top)

input()