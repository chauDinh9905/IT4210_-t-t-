#include "uart_printf.h"
#include <stdio.h>
#include <stdarg.h>
#include <string.h>

static UART_HandleTypeDef *s_huart = NULL;

void UART_Printf_Init(UART_HandleTypeDef *huart)
{
    s_huart = huart;
}

void UART_Printf(const char *fmt, ...)
{
    if (s_huart == NULL) return;

    char buf[64];
    va_list args;
    va_start(args, fmt);
    int len = vsnprintf(buf, sizeof(buf), fmt, args);
    va_end(args);

    if (len > 0)
    {
        HAL_UART_Transmit(s_huart, (uint8_t *)buf, (uint16_t)len, 100);
    }
}
