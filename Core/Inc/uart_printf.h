#ifndef UART_PRINTF_H
#define UART_PRINTF_H

#include "stm32f4xx_hal.h"

#ifdef __cplusplus
extern "C" {
#endif

void UART_Printf_Init(UART_HandleTypeDef *huart);
void UART_Printf(const char *fmt, ...);

#ifdef __cplusplus
}
#endif
#endif
