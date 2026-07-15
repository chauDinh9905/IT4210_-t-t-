#ifndef MODEL_HPP
#define MODEL_HPP

#include <stdint.h>

class ModelListener;

class Model
{
public:
    Model();

    void bind(ModelListener *listener)
    {
        modelListener = listener;
    }

    void tick();

    void setFinalScore(uint32_t score)
    {
        savedScore = score;
    }

    uint32_t getFinalScore()
    {
        return savedScore;
    }

    uint32_t updateAndGetHighScore();

protected:
    ModelListener *modelListener;

    uint32_t savedScore;
    uint32_t highScore;

    // PHẢI KHAI BÁO HAI HÀM NÀY
    uint32_t readHighScore();
    void writeHighScore(uint32_t score);
};

#endif // MODEL_HPP
