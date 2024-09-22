{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPgkDwlM3LOXNOcVlqttGul",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/mxng2/Boot_camp/blob/main/01_number_guess.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Y-dyCxiqHkVa",
        "outputId": "9b842e38-e96a-4bc5-8ec5-f16810edbd6a"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "에러가 발생했습니다. 숫자를 입력하세요\n",
            "에러가 발생했습니다. 숫자를 입력하세요\n"
          ]
        }
      ],
      "source": [
        "import random\n",
        "\n",
        "random_number = random.randint(1, 100)\n",
        "\n",
        "game_count = 1\n",
        "\n",
        "while True:\n",
        "    try:\n",
        "        my_number = int(input(\"1~100사이의 숫자를 입력하세요:\"))\n",
        "\n",
        "        if my_number > random_number:\n",
        "            print(\"다운\")\n",
        "        elif my_number < random_number:\n",
        "            print(\"업\")\n",
        "        elif my_number == random_number:\n",
        "            print(f\"축하합니다.{game_count}회 만에 맞췄습니다\")\n",
        "            break\n",
        "\n",
        "        game_count = game_count + 1\n",
        "\n",
        "    except:\n",
        "        print(\"에러가 발생했습니다. 숫자를 입력하세요\")\n",
        ""
      ]
    }
  ]
}