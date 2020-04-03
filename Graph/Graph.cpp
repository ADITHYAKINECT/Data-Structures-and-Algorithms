#include"Graph.h"

Graph::Graph(int V){
    if (V <= 0) throw "Number of Vertices should be Positive";
    else{
        this->V = V;
        this->E = 0;
        adj = new list<int>[V];     
    }   
}

Graph::Graph(const char* file_name){
    ifstream file(file_name);
    if (!file){
        throw "Cannot open the input file";
    }
    else{
        file>>V;
        file>>E;
        adj = new list<int>[V];
        int v,w;
        while(file >> v >> w){
            check_vertex(v);
            check_vertex(w);
            add_edge(v,w);
        }
    }    
}

void Graph::check_vertex(int v){
    if (v < 0 || v > V-1) throw "Vertex is not in the range";
}

int Graph::add_edge(int v, int w){
    check_vertex(v);
    check_vertex(w);
    E++;
    adj[v].push_front(w);
    adj[w].push_front(v);
}

list<int>::iterator Graph::show_adjacent_vetices(int v){
    check_vertex(v);
    list<int>::iterator lit;
    for (lit = adj[v].begin(); lit != adj[v].end(); ++lit){
        cout<<(*lit)<<" ";
    }
    cout<<"\n";
    return adj[v].begin(); 
}

int Graph::degree(int v){
    check_vertex(v);
    return adj[v].size();
}

int Graph::no_of_edges(){
    return E;
}

int Graph::no_of_vertices(){
    return V;
}

Graph::~Graph(){
    cout<<"Graph obejct deleted\n";
}

