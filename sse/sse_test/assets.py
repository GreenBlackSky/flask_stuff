from flask_assets import Bundle


def compile_assets(assets):
    js_bundle = Bundle('src/js/script.js', filters='jsmin', output='dst/js/script.min.js')
    assets.register('scripts_assets', js_bundle)
    js_bundle.build()

    css_bundle = Bundle('src/css/style.css', filters='cssmin', output='dst/css/style.min.css')
    assets.register('styles_assets', css_bundle)
    css_bundle.build()
