#include"Graph.h"

int main(int argc, char** argv){
    try{
        /*
        int v;
        cout<<"Enter the number of vertices: ";
        cin>>v;
        Graph* G = new Graph(v);
        G->add_edge(7,4);
        G->add_edge(7,5);
        G->add_edge(7,6);
        G->display(7);
        delete G;
        */
        char* file_mame = argv[1]; 
        Graph* G = new Graph(file_mame);
        cout<<G->no_of_vertices()<<"\n";
        G->display(11);
        delete G;
    }
    catch(const char* e){
        cout<< e << '\n';
    }
    return 0;
}