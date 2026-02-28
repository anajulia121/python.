#!/usr/bin/env python3

"""Simple example to generate an audio file with randomized
dynamic voice selection based on attributes such as Gender,
Language, or Locale."""

import asyncio
import random

import edge_tts
from edge_tts import VoicesManager

TEXT = "Escola integral é ruim, fora Lula, queremos picanha na merenda"
OUTPUT_FILE = "pt.mp3"


async def amain() -> None:
    """Main function"""
    voices = await VoicesManager.create()
    voice = voices.find(Gender="Male", Language="pt")
    # Also supports Locales
    # voice = voices.find(Gender="Female", Locale="es-AR")

    communicate = edge_tts.Communicate(TEXT, random.choice(voice)["Name"])
    await communicate.save(OUTPUT_FILE)


if __name__ == "__main__":
    asyncio.run(amain())