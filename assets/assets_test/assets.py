from flask_assets import Bundle


def compile_assets(assets):
    css_bundle = Bundle('src/css/style.css', filters='cssmin', output='dist/css/style.min.css')
    assets.register('styles_assets', css_bundle)
    css_bundle.build()

    js_bundle = Bundle('src/js/script.js', filters='jsmin', output='dist/js/script.min.js')
    assets.register('scripts_assets', js_bundle)
    js_bundle.build()
