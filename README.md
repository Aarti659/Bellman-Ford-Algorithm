//C++ Program to implement Bellman Ford Algorithm

#include <bits/stdc++.h> 

struct Edge 
{ 
    int src, dest, wei; 
}; 
struct Graph 
{ 
    int v, E; 
    struct Edge* edge; 
}; 
struct Graph* create(int v, int E) 
{ 
    struct Graph* graph = new Graph; 
    graph->v = v; 
    graph->E = E; 
    graph->edge = new Edge[E]; 
    return graph; 
} 
void chkres(int dist[], int n) 
{ 
    printf("Vertex   Distance from\n"); 
    for (int i = 0; i < n; ++i) 
        printf("%d \t %d\n", i, dist[i]); 
} 
  
void BellmanFord(struct Graph* graph, int src) 
{ 
    int v = graph->v; 
    int E = graph->E; 
    int dist[v]; 
    
    for (int i = 0; i < v; i++) 
        dist[i] = INT_MAX; 
    dist[src] = 0; 
  
    
    for (int i = 1; i <= v - 1; i++) { 
        for (int j = 0; j < E; j++) { 
            int u = graph->edge[j].src; 
            int v = graph->edge[j].dest; 
            int wei = graph->edge[j].wei; 
            if (dist[u] != INT_MAX && dist[u] + wei < dist[v]) 
                dist[v] = dist[u] + wei; 
        } 
    }  
    for (int i = 0; i < E; i++) 
    { 
        int u = graph->edge[i].src; 
        int v = graph->edge[i].dest; 
        int wei = graph->edge[i].wei; 
        if (dist[u] != INT_MAX && dist[u] + wei < dist[v])
        { 
            printf("Graph contains negative weight cycle");
            return;
        } 
    } 
    chkres(dist, v); 
    return; 
} 




  
int main() 
{
    int V = 4; 
    int E = 4;
    struct Graph* graph = create(V, E); 
    graph->edge[0].src = 0; 
    graph->edge[0].dest = 1; 
    graph->edge[0].wei = 3; 
    graph->edge[1].src = 0; 
    graph->edge[1].dest = 2; 
    graph->edge[1].wei = -2;
    graph->edge[2].src = 1; 
    graph->edge[2].dest = 2; 
    graph->edge[2].wei = 1; 
    graph->edge[3].src = 1; 
    graph->edge[3].dest = 3; 
    graph->edge[3].wei = 0; 
    BellmanFord(graph, 0); 
  
    return 0; 
}





