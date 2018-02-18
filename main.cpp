#include <iostream>

using namespace std;

void print_arr(char arr[3][3])
{
    cout<<"-------------"<<endl;
    for (int i=0; i<3; ++i)
    {
        for(int j=0 ; j<3 ; ++j)
        {
            if (j==0)
            {
                cout<<"| ";
            }
            cout<< arr[i][j]<<" | ";
        }
        cout<< endl;
        cout<<"-------------"<<endl;
    }
}

void check_num(int num,char arr[3][3],int player_num)
{
    while(num<0 || num>9)
    {
        cout<<"wrong"<<endl;
        print_arr(arr);
        cout<<"player "<<player_num<<","<<" enter number from 1 to 9 : ";
        cin>>num;
    }
}

void change_num(int &num)
{
    num+='0';
}

int main()
{
    char mat [3][3]=
    {
        {'1','2','3'},
        {'4','5','6'},
        {'7','8','9'}
    };
    char choise,player1,player2;
    cout<<"choise x or o"<<'\n';
    cin>>choise;
    bool flag=1;
    while(flag==1)
    {
        if(choise=='x' or choise=='X')
        {
            player1='x';
            player2='o';
            flag=0;
        }
        else if (choise=='o' or choise=='O')
        {
            player1='o';
            player2='x';
            flag=0;
        }
        else
        {
            cout<<"wrong choise"<<endl;
            cout<<"please choise x or o"<<endl;
            cin>>choise;
        }
    }

    int counter=0;
    int num;
    flag=1;
    while(counter<=8 && flag==1)
    {

        print_arr(mat);
        cout<<"player 1 , enter number from 1 to 9 : "<<endl;
        cin>>num;
        check_num(num,mat,1);
        change_num(num);

        bool test=0;
        for (int i=0 ; i<3 ; ++i)
        {
            for (int j=0 ; j<3 ; ++j)
            {
                if (mat[i][j]==num)
                {
                    mat[i][j]=player1;
                    test=1;
                }
            }
        }
        while(test==0)
        {
            cout<<"wrong"<<endl;
            print_arr(mat);
            cout<<"player 1 ,enter number from 1 to 9 : "<<endl;
            cin>>num;
            change_num(num);
            for (int i=0 ; i<3 ; ++i)
            {
                for (int j=0 ; j<3 ; ++j)
                {
                    if (mat[i][j]==num)
                    {
                        mat[i][j]=player1;
                        test=1;
                    }
                }
            }
        }
        print_arr(mat);
        for(int i=0; i<3 ; ++i)
        {
            if((mat[i][0]==mat[i][1]&&mat[i][1]==mat[i][2])||(mat[0][i]==mat[1][i]&&mat[1][i]==mat[2][i])||(mat[i][i]==mat[i+1][i+1]&&mat[i+1][i+1]==mat[i+2][i+2])||(mat[0][2]==mat[1][1]&&mat[1][1]==mat[2][0]))
            {
                cout<<"player 1 wins"<<endl;
                flag=0;
                break;
            }
        }
        if(flag==0)
        {
            break;
        }
        counter+=1;
        if (counter>8)
        {
            break;
        }

        //cout<<"counter 1 = "<<counter<<endl;
        //player2
        cout<<"player 2 , enter number from 1 to 9 : "<<endl;
        cin>>num;
        check_num(num , mat,2);
        change_num(num);
        test=0;
        for (int i=0 ; i<3 ; ++i)
        {
            for (int j=0 ; j<3 ; ++j)
            {
                if (mat[i][j]==num)
                {
                    mat[i][j]=player2;
                    test=1;
                }
            }
        }
        while(test==0)
        {
            cout<<"wrong"<<endl;
            print_arr(mat);
            cout<<"player 2 ,enter number from 1 to 9 : "<<endl;
            cin>>num;
            change_num(num);
            for (int i=0 ; i<3 ; ++i)
            {
                for (int j=0 ; j<3 ; ++j)
                {
                    if (mat[i][j]==num)
                    {
                        mat[i][j]=player2;
                        test=1;
                    }
                }
            }
        }
        counter+=1;
        for(int i=0; i<3 ; ++i)
        {
            if((mat[i][0]==mat[i][1]&&mat[i][1]==mat[i][2])||(mat[0][i]==mat[1][i]&&mat[1][i]==mat[2][i])||(mat[i][i]==mat[i+1][i+1]&&mat[i+1][i+1]==mat[i+2][i+2])||(mat[0][2]==mat[1][1]&&mat[1][1]==mat[2][0]))
            {
                cout<<"player 2 wins"<<endl;
                flag=0;
                break;
            }
        }
        if(flag==0)
        {
            break;
        }
    }
    if(counter>8)
    {
        cout<<"no winner"<<endl;
    }
    return 0;
}
