#ifndef AUDIO_MANAGER_H
#define AUDIO_MANAGER_H

#ifdef __cplusplus
extern "C" {
#endif

typedef enum
{
    AUDIO_START,
    AUDIO_SHOOT,
    AUDIO_HIT,
    AUDIO_DEAD,
    AUDIO_WIN,
    AUDIO_LOSE,
    AUDIO_FOOD,
    AUDIO_BUTTON
} AudioEvent;

void Audio_Play(AudioEvent event);

#ifdef __cplusplus
}
#endif

#endif
