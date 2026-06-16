#include <cstdint>
#include <cmath>
using namespace std;
extern "C"
{    
    void cmax(const uint8_t* arr, uint8_t* result, int row, int col, int a, int b, int c, int d)
    {
        for (int ch = 0; ch < 3; ch++)
        {
            for (int i = a; i < row - c; i++)
            {
                for (int j = b; j < col - d; j++)
                {
                    uint8_t maxi = 0;
                    for (int x = i - a;x <= i + c; x++)
                    {
                        for (int y = j - b;y <= j + d; y++)
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

    void cmin(const uint8_t* arr, uint8_t* result, int row, int col, int a, int b, int c, int d)
    {
        for (int ch = 0; ch < 3; ch++)
        {
            for (int i = a; i < row - c; i++)
            {
                for (int j = b; j < col - d; j++)
                {
                    uint8_t mini = 255;
                    for (int x = i - a;x <= i + c; x++)
                    {
                        for (int y = j - b;y <= j + d; y++)
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

    void cmode(const uint8_t* arr, uint8_t* result, int row, int col, int a, int b, int c, int d)
    {
        for (int ch = 0; ch < 3; ch++)
        {
            for (int i = a; i < row - c; i++)
            {
                for (int j = b; j < col - d; j++)
                {
                    int freq[256] = {0};
                    int maxi = 0;
                    for (int x = i - a;x <= i + c; x++)
                    {
                        for (int y = j - b;y <= j + d; y++)
                        {

                            freq[arr[(x * col + y) * 3 + ch]]++;
                            if (freq[arr[(x * col + y) * 3 + ch]] > maxi)
                            {
                                maxi = freq[arr[(x * col + y) * 3 + ch]];
                            }
                        }
                    }
                    int sum = 0;
                    int count = 0;
                    for (int z = 0; z < 256; z++)
                    {
                        if (maxi == freq[z])
                        {
                            sum += z;
                            count++;
                        }
                    }
                    result[(i * col + j) * 3 + ch] = static_cast<uint8_t>(sum /count);
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
