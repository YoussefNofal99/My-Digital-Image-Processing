#include <cstdint>
#include <algorithm>
#include <cstdint>
#include <vector>
#include <cmath>
using namespace std;
extern "C"
{    
    void cmax(const uint8_t* arr, uint8_t* result, int row, int col, int a, int b)
    {
        for (int ch = 0; ch < 3; ch++)
        {
            for (int i = a; i < row - a; i++)
            {
                for (int j = b; j < col - b; j++)
                {
                    uint8_t maxi = 0;
                    for (int x = i - a;x <= i + a; x++)
                    {
                        for (int y = j - b;y <= j + b; y++)
                        {
                            if (maxi < arr[(x * col + y) * 3 + ch])
                            {
                                maxi = arr[(x * col + y) * 3 + ch];
                            }
                        }
                    }
                    result[(i * col + j) * 3 + ch] = maxi;
                }
            }
        }
    }

    void cmin(const uint8_t* arr, uint8_t* result, int row, int col, int a, int b)
    {
        for (int ch = 0; ch < 3; ch++)
        {
            for (int i = a; i < row - a; i++)
            {
                for (int j = b; j < col - b; j++)
                {
                    uint8_t mini = 255;
                    for (int x = i - a;x <= i + a; x++)
                    {
                        for (int y = j - b;y <= j + b; y++)
                        {
                            if (mini > arr[(x * col + y) * 3 + ch])
                            {
                                mini = arr[(x * col + y) * 3 + ch];
                            }
                        }
                    }
                    result[(i * col + j) * 3 + ch] = mini;
                }
            }
        }
    }

    void cmode(const uint8_t* arr, uint8_t* result, int row, int col, int a, int b)
    {
        for (int ch = 0; ch < 3; ch++)
        {
            for (int i = a; i < row - a; i++)
            {
                for (int j = b; j < col - b; j++)
                {
                    vector<pair<int, uint8_t> > freq(256, {0, 0});
                    for (int x = i - a;x <= i + a; x++)
                    {
                        for (int y = j - b;y <= j + b; y++)
                        {
                            freq[arr[(x * col + y) * 3 + ch]].first++;
                            freq[arr[(x * col + y) * 3 + ch]].second = arr[(x * col + y) * 3 + ch];
                        }
                    }
                    sort(freq.begin(), freq.end());
                    uint8_t mode = freq[255].second;
                    int sum = freq[255].second;
                    int count = 1;
                    int z = 255;
                    while(z > 0 && freq[z].first == freq[z - 1].first)
                    {
                        z--;
                        sum += freq[z].second;
                        count++;
                    }
                    mode = sum / count;
                    result[(i * col + j) * 3 + ch] = static_cast<uint8_t>(mode);
                }
            }
        }
    }

    void cprewitt(const uint8_t* arr, uint8_t* result, int row, int col)
    {
        int h1[3][3] = {{-1, 0, 1}, 
                        {-1, 0, 1}, 
                        {-1, 0, 1}};
        int h2[3][3] = {{-1, -1, -1}, 
                        { 0,  0,  0}, 
                        { 1,  1,  1}};
        for (int i = 1; i < row - 1; i++)
        {
            for (int j = 1; j < col - 1; j++)
            {
                int sum1 = 0;
                int sum2 = 0;
                for (int x = i - 1;x <= i + 1; x++)
                {
                    for (int y = j - 1;y <= j + 1; y++)
                    {
                        sum1 += arr[(x * col + y)] * h1[x - i + 1][y - j + 1];
                        sum2 += arr[(x * col + y)] * h2[x - i + 1][y - j + 1];
                    }
                }
                int temp = sqrt(sum1 * sum1 + sum2 * sum2);
                if (temp > 255)
                {
                    temp = 255;
                }
                result[(i * col + j)] = static_cast<uint8_t>(temp);
            }
        }
    }

    void croberts(const uint8_t* arr, uint8_t* result, int row, int col)
    {
        int h1[2][2] = {{-1, 0}, 
                        { 0, 1}};
        int h2[2][2] = {{0, -1}, 
                        {1,  0}};
        for (int i = 1; i < row; i++)
        {
            for (int j = 1; j < col; j++)
            {
                int sum1 = 0;
                int sum2 = 0;
                for (int x = i - 1;x <= i; x++)
                {
                    for (int y = j - 1;y <= j; y++)
                    {
                        sum1 += arr[(x * col + y)] * h1[x - i + 1][y - j + 1];
                        sum2 += arr[(x * col + y)] * h2[x - i + 1][y - j + 1];
                    }
                }
                int temp = sqrt(sum1 * sum1 + sum2 * sum2);
                if (temp > 255)
                {
                    temp = 255;
                }
                result[(i * col + j)] = static_cast<uint8_t>(temp);
            }
        }
    }
}