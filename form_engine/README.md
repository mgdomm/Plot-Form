# Form Engine

The Form Engine generates visual elements including mandalas and illustrations for creative books.

## Features (Planned)

- Mandala pattern generation
- Illustration creation from narrative prompts
- Visual style customization
- SVG and raster image output

## Usage

```python
from form_engine.mandala_generator import MandalaGenerator
from form_engine.illustration_generator import IllustrationGenerator

# Generate a mandala
mandala_gen = MandalaGenerator(symmetry=8)
mandala = mandala_gen.generate(complexity="medium")

# Generate an illustration
illustration_gen = IllustrationGenerator()
illustration = illustration_gen.generate("A mystical forest scene", style="minimalist")
```

## Status

🚧 Under Development
