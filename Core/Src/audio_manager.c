#include "audio_manager.h"
#include "uart_printf.h"

void Audio_Play(AudioEvent event)
{
    switch(event)
    {
        case AUDIO_START:
            UART_Printf("SOUND:START\r\n");
            break;

        case AUDIO_SHOOT:
            UART_Printf("SOUND:SHOOT\r\n");
            break;

        case AUDIO_HIT:
            UART_Printf("SOUND:HIT\r\n");
            break;

        case AUDIO_DEAD:
            UART_Printf("SOUND:DEAD\r\n");
            break;

        case AUDIO_WIN:
            UART_Printf("SOUND:WIN\r\n");
            break;

        case AUDIO_LOSE:
            UART_Printf("SOUND:LOSE\r\n");
            break;

        case AUDIO_FOOD:
            UART_Printf("SOUND:FOOD\r\n");
            break;

        case AUDIO_BUTTON:
            UART_Printf("SOUND:BUTTON\r\n");
            break;

        default:
            break;
    }
}
