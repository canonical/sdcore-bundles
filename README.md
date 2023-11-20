# SD-Core bundles
[![CharmHub Badge](https://charmhub.io/sdcore/badge.svg)](https://charmhub.io/sdcore)
[![CharmHub Badge](https://charmhub.io/sdcore-control-plane/badge.svg)](https://charmhub.io/sdcore-control-plane)
[![CharmHub Badge](https://charmhub.io/sdcore-user-plane/badge.svg)](https://charmhub.io/sdcore-user-plane)

This project contains charm bundles for SD-Core. 

### Bundle generation

To render a bundle and output it in the bundle directory (e.g., `SDCORE_USER_PLANE`):

```bash
pip3 install -r render_bundle/requirements.txt
python3 render_bundle/render_bundle.py --bundle_variant SDCORE_USER_PLANE --output_file bundle/bundle.yaml
```
