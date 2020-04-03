#ifndef GRAPH_H
#define GRAPH_H
#include<iostream>
#include<list>
#include<string>
#include<fstream>
using namespace std;

class Graph{
    int E;
    int V;
    list<int>* adj;
    private:

    public:
        Graph(int V);
        Graph(const char* file_name);
        int no_of_edges();
        int no_of_vertices();
        int add_edge(int v, int w);
        list<int>::iterator show_adjacent_vetices(int v);
        int degree(int v);
        void check_vertex(int v);
        ~Graph();
};

#endif