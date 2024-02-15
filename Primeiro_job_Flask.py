{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyP9auBFg9u3XWn2FG4c6eZZ"
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
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "BvFG63vJpZB6"
      },
      "outputs": [],
      "source": [
        "import flask\n",
        "from flask import Flask\n",
        "app = Flask(__name__)\n",
        "\n",
        "@app.route(\"/\")\n",
        "def home():\n",
        "    return \"Testando Flask!\"\n",
        "\n",
        "if __name__ == \"__main__\":\n",
        "    app.run(debug=True)"
      ]
    }
  ]
}