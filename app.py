from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')
 
@app.route('/')
def home():
    return render_template('index.html')
 
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/help')
def help_page():
    return render_template('help.html')

@app.route('/donate')
def donate():
    return render_template('donate.html')

@app.route('/dmca')
def dmca():
    return render_template('dmca.html')

@app.route('/cookies')
def cookies():
    return render_template('cookies.html')

@app.route('/disclaimer')
def disclaimer():
    return render_template('disclaimer.html')

@app.route('/report-bug')
def report_bug():
    return render_template('report-bug.html')

@app.route('/feature-request')
def feature_request():
    return render_template('feature-request.html')

@app.route('/blog/')
def blog_index():
    return render_template('blog/index.html')

# --- Tool Categories Index Pages ---
@app.route('/all-tools')
def all_tools():
    return render_template('all-tools.html')

@app.route('/social-media-tools/')
def social_media_index():
    return render_template('social-media-tools/index.html')

@app.route('/editors/')
def editors_index():
    return render_template('editors/index.html')

@app.route('/converters/')
def converters_index():
    return render_template('converters.html')

@app.route('/productivity-tools/')
def productivity_index():
    return render_template('productivity-tools.html')

@app.route('/dev-tools/')
def dev_tools_index():
    return render_template('dev-tools/index.html')

@app.route('/games/')
def games_index():
    return render_template('games/index.html')

@app.route('/date-time-tools/')
def date_time_index():
    return render_template('date-time-tools/index.html')

@app.route('/mathematical-tools/')
def math_index():
    return render_template('mathematical-tools/index.html')

@app.route('/store')
def store():
    return render_template('store.html')  # Assuming this exists

@app.route('/d2karmy')
def d2karmy():
    return render_template('d2karmy.html')  # Assuming this exists

# --- Social Media Tools ---
@app.route('/social-media-tools/youtube-thumbnail-downloader')
def youtube_thumbnail_downloader():
    return render_template('social-media-tools/youtube-thumbnail-downloader.html')

@app.route('/social-media-tools/youtube-shorts-downloader')
def youtube_shorts_downloader():
    return render_template('social-media-tools/youtube-shorts-downloader.html')

@app.route('/social-media-tools/youtube-video-downloader')
def youtube_video_downloader():
    return render_template('social-media-tools/youtube-video-downloader.html')

@app.route('/social-media-tools/youtube-shorts-and-video-downloader')
def youtube_shorts_and_video_downloader():
    return render_template('social-media-tools/youtube-shorts-and-video-downloader.html')

# --- Converters ---
@app.route('/converters/to-pdf')
def converter_to_pdf():
    return render_template('converters/to-pdf.html')

@app.route('/converters/to-jpg')
def converter_to_jpg():
    return render_template('converters/to-jpg.html')

@app.route('/converters/pdf-to-png')
def converter_pdf_to_png():
    return render_template('converters/pdf-to-png.html')

@app.route('/converters/to-ico')
def converter_to_ico():
    return render_template('converters/to-ico.html')

@app.route('/converters/to-png')
def converter_to_png():
    return render_template('converters/to-png.html')

@app.route('/converters/to-webp')
def converter_to_webp():
    return render_template('converters/to-webp.html')

@app.route('/converters/to-jpeg')
def converter_to_jpeg():
    return render_template('converters/to-jpeg.html')

@app.route('/converters/to-heif')
def converter_to_heif():
    return render_template('converters/to-heif.html')

# --- Compilers ---
@app.route('/compilers/')
def compilers_index():
    return render_template('compilers/index.html')

@app.route('/compilers/html')
def compiler_html():
    return render_template('compilers/html.html')

@app.route('/compilers/c')
def compiler_c():
    return render_template('compilers/c.html')

@app.route('/compilers/cpp')
def compiler_cpp():
    return render_template('compilers/cpp.html')

@app.route('/compilers/java')
def compiler_java():
    return render_template('compilers/java.html')

@app.route('/compilers/js')
def compiler_js():
    return render_template('compilers/js.html')

@app.route('/compilers/python')
def compiler_python():
    return render_template('compilers/python.html')

@app.route('/compilers/sql')
def compiler_sql():
    return render_template('compilers/sql.html')

@app.route('/compilers/text-editor')
def compiler_text_editor():
    return render_template('compilers/text-editor.html')

# --- Productivity Tools ---
@app.route('/productivity-tools/daily-planner')
def productivity_daily_planner():
    return render_template('productivity-tools/daily-planner.html')

@app.route('/productivity-tools/calendar-view')
def productivity_calendar_view():
    return render_template('productivity-tools/calendar-view.html')

@app.route('/productivity-tools/checklist-generator')
def productivity_checklist_generator():
    return render_template('productivity-tools/checklist-generator.html')

@app.route('/productivity-tools/distraction-blocker')
def productivity_distraction_blocker():
    return render_template('productivity-tools/distraction-blocker.html')

 
@app.route('/games/sudoku')
def game_sudoku():
    return render_template('games/sudoku.html')

@app.route('/games/chess')
def game_chess():
    return render_template('games/chess.html')

@app.route('/games/2048')
def game_2048():
    return render_template('games/2048.html')

@app.route('/games/wordle')
def game_wordle():
    return render_template('games/wordle.html')

@app.route('/games/freely-car')
def game_freely_car():
    return render_template('games/freely-car.html')

@app.route('/games/memory-game')
def game_memory_game():
    return render_template('games/memory-game.html')

@app.route('/games/tic-tac-toe')
def game_tictactoe():
    return render_template('games/tic-tac-toe.html')

# --- Date Time Tools ---
@app.route('/date-time-tools/alarm-clock')
def alarm_clock():
    return render_template('date-time-tools/alarm-clock.html')

@app.route('/date-time-tools/calendar')
def calendar_tool():
    return render_template('date-time-tools/calendar.html')

@app.route('/date-time-tools/countdown-timer')
def countdown_timer():
    return render_template('date-time-tools/countdown-timer.html')

@app.route('/date-time-tools/date-calculator')
def date_calculator():
    return render_template('date-time-tools/date-calculator.html')

@app.route('/date-time-tools/digital-clock')
def digital_clock():
    return render_template('date-time-tools/digital-clock.html')

@app.route('/date-time-tools/stopwatch')
def stopwatch():
    return render_template('date-time-tools/stopwatch.html')

@app.route('/date-time-tools/time-zone-converter')
def time_zone_converter():
    return render_template('date-time-tools/time-zone-converter.html')

@app.route('/date-time-tools/world-clock')
def world_clock():
    return render_template('date-time-tools/world-clock.html')

# --- Dev Tools ---
@app.route('/dev-tools/base64-encoder')
def base64_encoder():
    return render_template('dev-tools/base64-encoder.html')

@app.route('/dev-tools/css-obfuscator')
def css_obfuscator():
    return render_template('dev-tools/css-obfuscator.html')

@app.route('/dev-tools/js-obfuscator')
def js_obfuscator():
    return render_template('dev-tools/js-obfuscator.html')

@app.route('/dev-tools/json-formatter')
def json_formatter():
    return render_template('dev-tools/json-formatter.html')

# --- Editors ---
@app.route('/editors/compress-image')
def compress_image():
    return render_template('editors/compress-image.html')

@app.route('/editors/compress-pdf')
def compress_pdf():
    return render_template('editors/compress-pdf.html')

@app.route('/editors/image-crop')
def image_crop():
    return render_template('editors/image-crop.html')

@app.route('/editors/improve-pdf-quality')
def improve_pdf_quality():
    return render_template('editors/improve-pdf-quality.html')

@app.route('/editors/pdf-upscaler-enhancer')
def pdf_upscaler():
    return render_template('editors/pdf-upscaler-enhancer.html')

@app.route('/editors/image-resizer')
def image_resizer():
    return render_template('editors/image-resizer.html')

@app.route('/editors/image-shape-croper')
def image_shape_croper():
    return render_template('editors/image-shape-croper.html')

# --- Mathematical Tools ---
@app.route('/mathematical-tools/calculator')
def calculator():
    return render_template('mathematical-tools/calculator.html')

@app.route('/mathematical-tools/equation-solver')
def equation_solver():
    return render_template('mathematical-tools/equation-solver.html')

@app.route('/mathematical-tools/graphing-calculator')
def graphing_calculator():
    return render_template('mathematical-tools/graphing-calculator.html')

@app.route('/mathematical-tools/matrix-calculator')
def matrix_calculator():
    return render_template('mathematical-tools/matrix-calculator.html')

@app.route('/mathematical-tools/percentage-calculator')
def percentage_calculator():
    return render_template('mathematical-tools/percentage-calculator.html')

@app.route('/mathematical-tools/scientific-calculator')
def scientific_calculator():
    return render_template('mathematical-tools/scientific-calculator.html')

@app.route('/mathematical-tools/unit-converter')
def unit_converter():
    return render_template('mathematical-tools/unit-converter.html')
 
if __name__ == '__main__':
    app.run(debug=True)