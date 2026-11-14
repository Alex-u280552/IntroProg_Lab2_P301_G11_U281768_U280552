"""
PONG Template for Lab2 (Introduction to Programming)
---------------------------------------------------------
Didactic objectives (focus on functions):
- Practice defining and using functions using parameters and return values.
- Avoid global variables.
- Chain functions that transform the game state (positions and velocities).
- DO NOT use classes, lists, or dictionaries.
- Fill the code where needed. Keep functions' names and signatures EXACT.

Submission:
- Through your team's GitHub repository (see Section 9 of the Lab 2 instructions).
- Save this file in the repository as: pong.py
- Must run locally with: `python pong.py` (macOS: `python3 pong.py`)
- Requires pygame-ce (install with `python -m pip install pygame-ce`).
  Your code still uses `import pygame`.

Restrictions / Style rules:
- No `class`, no `list`, no `dict` (tuples are allowed for multiple returns).
- Do not use `assert` or define classes. Simple string methods such as
  `.lower()` or `.strip()` are allowed.
- Define and use the functions marked TODO. Do not rename them.
- Constants can be read but NOT modified at runtime.
- The main loop and rendering section are provided; do not change or move them,
  except where an optional feature requires it (explain any change in your report).

Anti-AI-copy/paste control:
- You must be able to explain to the professor what each function does
- You must be able to explain specific sections of your program to the professor to verify your understanding
- If you used AI tools, explain how in your report (section "Use of AI tools")
"""

import sys      # Used only for sys.exit(0): ensures clean program termination on all OSs
import pygame   # essential for all the game rendering and play
import random   # useful for randomising things a little bit (e.g. ball's initial direction)

# ==============
# Game constants
# ==============

# Modify them here if you want to change the board size 
WIDTH = 900     # pixels   
HEIGHT = 600    # idem
FPS = 60        # Frames per Second - No need to change - for changing paddles/ball speeds change the following ->

# Speeds (pixels per frame approx.) (all 3 values can be changed in get_config() )
SPEED_PADDLE = 7
SPEED_BALL_X = 6
SPEED_BALL_Y = 5

# Background and Foreground RGB default colors (can be changed in change_colors() )
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Geometry: paddle and ball default values (some can be changed in get_config() )
PADDLE_W = 14       # pixels
PADDLE_H = 110      # 110 pixels - can be changed in get_config()
PADDLE_MARGIN = 30  # pixels - distance from border
BALL_RADIUS = 9     # pixels - can be changed in get_config()
POINTS_END = 5      # score for ending a match
SERVE_PAUSE = 300   # ms between each serve

# Player keys: Change here if other keys are preferred
KEY_UP_LEFT = pygame.K_a            # a
KEY_DOWN_LEFT = pygame.K_z          # z
KEY_UP_RIGHT = pygame.K_UP          # arrow UP
KEY_DOWN_RIGHT = pygame.K_DOWN      # arrow DOWN

# Play against machine (optional feature): set to True once compute_ai_direction() is implemented
PLAY_AGAINST_MACHINE = False

# ==============================================================================
# Functions to complete by the students : configuration/setup before game starts
# ==============================================================================

def get_config() -> tuple[int, int, int, int, int]:
    """ Ask the user whether they want to modify the main game parameters:
    (paddle height, paddle speed, ball X speed, ball Y speed, and ball radius).
   
    If the user chooses **not** to open the configuration menu, the function
    simply returns the default constant values defined at the top of the program:
        (PADDLE_H, SPEED_PADDLE, SPEED_BALL_X, SPEED_BALL_Y, BALL_RADIUS)

    If the user answers **yes**, the function should:
      - For each configurable value, call `read_int_in_range()` to ask for a new number
        within reasonable limits (for example: paddle height between 60-160).
      - Collect the five resulting integers and return them together in the following order:
            (paddle_height, paddle_speed, ball_x_speed, ball_y_speed, ball_radius)

    Parameters
    ----------
    None

    Returns
    -------
    int, int, int, int, int : 
        the selected configuration values in the specified order ->
        paddle_height, paddle_speed, ball_x_speed, ball_y_speed, ball_radius

    Notes and hints
    ---------------
    - Use `ask_yes_no(prompt)` to decide whether to open the menu.
    - Use `read_int_in_range(prompt, low, high)` to read each numeric value.
    - Keep the function free of global assignments: it should only **return**
      the chosen values, not modify constants.
    - Remember to maintain the same order of the returned elements.
    """

    # TODO: put your code!!!!

    # This line of code has been left for letting the full program work
    # It corresponds to the user answering NO to changing any default values 
    # You will need to eliminate it when adding your code
    return PADDLE_H, SPEED_PADDLE, SPEED_BALL_X, SPEED_BALL_Y, BALL_RADIUS 

def change_colors() -> tuple[tuple[int, int, int], tuple[int, int, int]]:
    """ Ask the user if they want to modify the game colors (background and foreground).

    If the user chooses **not** to change colors, return the default color tuples:
        (BLACK, WHITE)

    If the user answers **yes**, the function should:
      - Ask for a new **background** color.
      - Ask for a new **foreground** color (the color used for paddles, ball, and text).
      - Each color must be entered as a tuple of three integers
        representing the RGB components (Red, Green, Blue),
        with each value between 0 and 255.

    Parameters
    ----------
    None

    Returns
    -------
    tuple[tuple[int, int, int], tuple[int, int, int]]
        Two RGB color tuples: (background_color, foreground_color)

    Notes and hints
    ---------------
    - Use `ask_yes_no(prompt)` to decide whether to open the color configuration.
    - Use `read_color(prompt)` to read one color at a time.
      This function should itself ask for the three RGB components.
    - Remember that colors in pygame are defined as tuples of 3 integers: (red, green, blue)
    - Keep the order of returned values consistent: first background, then foreground.
    """

    # TODO: put your code!!!!

    # This line of code has been left for letting the full program work
    # You will need to eliminate it when adding your code
    return BLACK, WHITE

def read_color(prompt: str) -> tuple[int, int, int]:
    """Ask the user to enter the three RGB components of a color with each component in [0,255].
    The function receives a short text (for example: "background" or "foreground")
    that identifies which color is being configured.

    For each of the three color components — Red, Green, and Blue —
    the function should ask the user to enter an integer between 0 and 255
    (both included). Use the helper function `read_int_in_range()` to
    safely read each component.

    Parameters
    ----------
    prompt : str
        A word describing the color to be read (e.g. "background", "foreground").

    Returns
    -------
    int, int, int
        A tuple (r, g, b) representing the color chosen by the user,
        where each component is an integer in the range [0, 255].

    Notes and hints
    ---------------
    - Call `read_int_in_range()` three times, once for each component (Red, Green, Blue).
    - Return all three integers together as a single tuple.
    - In pygame, colors are always expressed as (R, G, B) tuples.
    - Keep the order (Red, then Green, then Blue).
    """ 

    # TODO: put your code!!!!
    # return r, g, b

def read_int_in_range(prompt: str, low: int, high: int) -> int:
    """Ask user for an integer within [low, high]. 
    Keeps asking until a valid value is entered.
    The implementation must not stop the program due to an error.
    Should be robust to out-of-range numbers and non-integer input.

    Parameters
    ----------
    prompt : str
        The message that will appear before the user types input.
        Example: "Enter paddle height".
    low : int
        The minimum allowed integer value.
    high : int
        The maximum allowed integer value.

    Returns
    -------
    An integer value such that low <= value <= high.
    """
    
    # TODO: put your code!!!!
    while True:
        try: 
            #   Sol·licitud d'entrada a l'usuari amb indicació del rang
            user_input = input(f"{prompt} - Introdueix un valor entre {low} i {high}: ").strip()  # S'imprimeix la pregunta amb la indicació de com respondre (valor entre low i high) i es llegeix l'entrada de l'usuari. Amb strip() eliminem els espais en blanc al principi i al final de la resposta per evitar que sigui " 100 " i es consideri invàlida.

            #   Gestió de la resposta de l'usuari i comprovació de la validesa de l'entrada
            if low <= int(user_input) <= high:  # Comprovem si l'entrada de l'usuari es situa entre els valors del rang
                return int(user_input)  # Si el valor introduit per l'usuari es troba dins del rang, es retorna aquest valor i es surt del bucle
            elif int(user_input) < low or int(user_input) > high:  # Comprovem si l'entrada de l'usuari és fora del rang especificat
                print(f"Introdueix un valor entre {low} i {high}.")  # Si el valor introduit per l'usuari es troba fora del rang, es mostra un missatge d'error indicant que l'entrada no és vàlida i es torna a demanar la resposta

        #   Gestió de l'error
        except ValueError:  # Si l'entrada de l'usuari no és un enter (lletres, decimals o cap valor), es captura l'excepció ValueError
            print("Introdueix un valor vàlid.")  # Es mostra un missatge d'error indicant que l'entrada no és vàlida i es torna a demanar la resposta

def read_int_in_range_w_default(prompt: str, low: int, high: int, default_val: int) -> int:
    """ Advanced/alternate more user-friendly version of read_int_in_range().
    Works like the basic version, but adds support for a *default value*.
    You can do it as a substitute, but we recommend you to start with the basic one

    If the user simply presses ENTER without typing anything,
    the function immediately returns `default_val` **without asking again**.

    Behavior summary:
      - Ask the user for an integer in the range [low, high].
      - If the user enters a valid number, return it.
      - If the user presses ENTER directly, return `default_val`.
      - If the user enters text or an out-of-range number, print an error
        message and repeat the question.

    Parameters
    ----------
    prompt : str
        Message shown to the user before input.
    low : int
        Minimum allowed integer value.
    high : int
        Maximum allowed integer value.
    default_val : int
        Value returned when the user presses ENTER without typing anything.
        It should be inside the range [low, high].
        Take the value from the CONSTANT defined at the beginning

    Returns
    -------
    int
        The integer entered by the user, or `default_val` if the user pressed ENTER.
    """
    
    # TODO: put your code!!!!

    while True:
        try: 
            #   Sol·licitud d'entrada a l'usuari amb indicació del rang i del valor per defecte
            user_input = input(f"{prompt} - Introdueix un valor entre {low} i {high}, en cas de voler el valor per defecte ({default_val}), prem ENTER: ").strip()  # S'imprimeix la pregunta amb la indicació de com respondre (valor entre low i high, o ENTER per defecte) i es llegeix l'entrada de l'usuari. Amb strip() eliminem els espais en blanc al principi i al final de la resposta per evitar que sigui " 100 " i es consideri invàlida.

            #   Gestió de la resposta de l'usuari i comprovació de la validesa de l'entrada
            if user_input == "":  # Comprovem si l'usuari ha premut ENTER sense introduir cap valor
                return default_val  # Si l'usuari ha premut ENTER sense introduir cap valor, es retorna el valor per defecte i es surt del bucle
            elif low <= int(user_input) <= high:  # Comprovem si l'entrada de l'usuari es situa entre els valors del rang
                return int(user_input)  # Si el valor introduit per l'usuari es troba dins del rang, es retorna aquest valor i es surt del bucle
            elif int(user_input) < low or int(user_input) > high:  # Comprovem si l'entrada de l'usuari és fora del rang especificat
                print(f"Introdueix un valor entre {low} i {high}.")  # Si el valor introduit per l'usuari es troba fora del rang, es mostra un missatge d'error indicant que l'entrada no és vàlida i es torna a demanar la resposta

        #   Gestió de l'error
        except ValueError:  # Si l'entrada de l'usuari no és un enter, es captura l'excepció ValueError
            print("Introdueix un valor vàlid.")  # Es mostra un missatge d'error indicant que l'entrada no és vàlida i es torna a demanar la resposta

def ask_yes_no(prompt: str) -> bool:
    """ Ask the user a yes/no question and return the corresponding Boolean value.

    The function should repeatedly prompt the user until a valid answer
    is given. It must accept both upper- and lowercase input, and it should
    not crash on unexpected text.

    Parameters
    ----------
    prompt : str
        The question to show to the user (for example: "Change colors?").
        The function should append "(y/n):" or similar guidance to the prompt
        when displaying it.

    Returns
    -------
    bool
        True  → if the user answered "y" or "yes"
        False → if the user answered "n" or "no"

    Notes and hints
    ---------------
    - Accept short forms ("y", "n") and optionally full words ("yes", "no").
    - Accept also UPPERCASE, so better convert user input to lowercase
    - Print a short message (e.g. "Please answer y/n.") when the answer is invalid.
    - Return only after receiving a valid input; do not stop the program with errors.
    """
    # TODO: put your code!!!!
 
    while True:
  
        answer = input(prompt + " (y/n): ")  # S'imprimeix la pregunta amb la indicació de com respondre (y/n)
        # Transformem la resposta a minúscules i eliminem els espais en blanc al principi i al final per tal de poder processar-la
        answer = answer.strip().lower()  # Amb strip() eliminem els espais en blanc al principi i al final de la resposta, i amb lower() convertim els caràcters de la resposta en minúscules.

        # Processem la resposta de l'usuari i comprovem si és vàlida
        if answer == "y" or answer == "yes":  # Comprovem si la resposta és sí (y o yes)
            return True  # Es retorna True si la resposta és afirmativa, es surt del bucle
        elif answer == "n" or answer == "no": # Comprovem si la resposta és no (n o no)
            return False  # Es retorna False si la resposta és negativa, es surt del bucle
        else:  # Si la resposta no és ni sí ni no tal i com s'especifica en les instruccions, es torna a demanar
            print("Introdueix una resposta vàlida (y/n).")  # Es mostra un missatge d'error indicant que la resposta no és vàlida i es torna a demanar la resposta

# ================================
# Functions to complete: main game
# ================================

def move_paddle(current_y: int, direction: int, speed: int, height: int, paddle_h: int) -> int:
    """Return new y coordinate of a paddle, updating current position
    Parameters:
        current_y - current top position of the paddle (pixels)
        direction - movement direction: -1 (up), 0 (no move), +1 (down)
        speed     - number of pixels to move per frame (speed is always positive. It will be up or down depending on direction)
        height    - height of the board
        paddle_h  - height of the paddle
    Returns:
        new_y     - updated y position (pixels)
    
    Take into account that the paddle must always stay fully visible on screen.
    That is when it reaches the limits (up or down) it stays there, so consider paddle_h and height here.
    """
    # 1. Calcular la posició nova
    # speed sempre és positiu; direction (-1, 0 o +1) n'indica el sentit.
    # En multiplicar-los, el desplaçament és negatiu (puja), zero (quieta) o positiu (baixa).
    new_y = current_y + direction * speed

    # 2. Límit superior: la vora de dalt de la pala (new_y) no pot ser menor que 0
    if new_y < 0:
        new_y = 0

    # 3. Límit inferior: la vora de baix (new_y + paddle_h) no pot passar de height,
    #    per tant la y màxima de la pala és height - paddle_h
    elif new_y > height - paddle_h:
        new_y = height - paddle_h

    # 4. Retornar la posició ja corregida (el bucle principal la desa a p1_y o p2_y)
    return new_y


def move_ball(x: int, y: int, vx: int, vy: int) -> tuple[int, int]:
    """Move the ball one time step. Return (x', y').
    Parameters:
        x  - current horizontal position of the ball (pixels)
        y  - current vertical position of the ball (pixels)
        vx - horizontal speed (pixels increment at each step)
        vy - vertical speed (pixels increment at each step)
    Returns:
        new_x, new_y - updated horizontal and vertical position (pixels)
    
    Note that collisions (i.e. with the paddles, with the walls) are not considered yet here, 
    but in the next 2 functions (collide_ball_walls and collide_ball_paddle)
    """

    # TODO: put your code!!!!
    # 1. Nova posició horitzontal (eix x)
    new_x = x + vx  # La nova posició de x és el valor actual de x més la velocitat horitzontal de vx

    # 2. Nova posició vertical (eix y)
    new_y = y + vy  # La nova posició és el valor actual de y més la velcitat vertical de vy

    # 3. Es retornen les noves coordenades (x', y') de la pilota després del moviment 
    # !Seguint les indicacions, no es fa cap comprovació de col·lisions aquí, només es mou la pilota!
    return new_x, new_y # Es retornen les noves coordenades (new_x, new_y) de la pilota després del moviment


def collide_ball_walls(x: int, y: int, vx: int, vy: int, radius: int, width: int, height: int) -> tuple[int, int, int, int]:
    """Detect and handle collisions with top/bottom walls.
    Parameters:
        x       - current horizontal position of the ball (pixels)
        y       - current vertical position of the ball (pixels)
        vx      - horizontal speed (pixels increment at each step)
        vy      - vertical speed (pixels increment at each step)
        radius  - of the ball (pixels)
        width   - of the board (pixels). Not needed here: goals are handled in main()
        height  - of the board (pixels)
    Returns:
        updated x, y, vx, vy
    Rules:
        Make sure the ball stays inside the area.
        Do not consider "goals" (ball hitting vertical walls) here. Check only horizontal bounces on top/bottom walls
        When hitting a horizontal wall, change the sign of vy
        For precisely detecting collisions, you might need to consider the ball radius
    """
    # TODO: put your code!!!!
    # Aclariment: la pantalla en l'eix y es considera amb 0 a dalt i "height" a baix. Per tant, la vora superior de la pilota és y - radius i la vora inferior és y + radius.
    # Dibuixem la pilota amb centre a (x,y) amb un radi segons la variable "radius"

    # Vora superior de la pilota
    if y - radius < 0:  # Si la vora superior de la pilota és més petita que 0 (fora de la pantalla)
        y = radius  # La nova posició vertical de la pilota és el radi (la vora superior toca el límit superior)
        vy = -vy  # Invertim la velocitat vertical per simular el rebot (canviem el signe de vy per canviar-ne el sentit)

    # Vora inferior de la pilota
    if y + radius > height:  # Si la vora inferior de la pilota és més gran que l'altura de la pantalla
        y = height - radius  # La nova posició vertical de la pilota és l'altura menys el radi (la vora inferior toca el límit inferior)
        vy = -vy  # Invertim la velocitat vertical per simular el rebot (canviem el signe de vy per canviar-ne el sentit)

    # En aquesta funció només es comproven les col·lisions amb les parets horitzontals (superior i inferior) ja que les verticals es tracten en el main ja que són els gols. 
    # Es retornen les noves coordenades (x, y) i velocitats (vx, vy) de la pilota després de comprovar les col·lisions amb les parets.
    return x, y, vx, vy 


def collide_ball_paddle(x: int, y: int, vx: int, vy: int, paddle_x: int, paddle_y: int, paddle_w: int, paddle_h: int, radius: int) -> tuple[int, int, int, int, bool]:
    """
    Detect and handle a collision between the ball and a paddle
    using a simple AABB (Axis-Aligned Bounding Box) approximation.

    Parameters
    ----------
    x, y : Current position of the CENTER of the ball (in pixels).
           Remember: (0,0) is the top-left corner of the screen.
    vx, vy : Current horizontal and vertical speed of the ball (pixels per frame).
    paddle_x, paddle_y : Top-left corner of the paddle.
    paddle_w, paddle_h : Width and height of the paddle.
    radius : Radius of the ball.

    Returns
    -------
    x_new, y_new : Possibly corrected position of the ball (e.g. moved just outside the paddle).
    vx_new, vy_new : Possibly modified velocities. vx is inverted if collision occurs.
    hit : True if a collision occurred, False otherwise.

    Algorithm and hints
    -------------------
    1. Approximate the circular ball by a small square defined by:
           left   = x - radius
           right  = x + radius
           top    = y - radius
           bottom = y + radius
       This makes collision checks simpler: rectangles only.

    2. Compare this "ball box" with the paddle rectangle defined by:
           left   = paddle_x
           right  = paddle_x + paddle_w
           top    = paddle_y
           bottom = paddle_y + paddle_h
       A collision happens when the two rectangles overlap.

    3. If they overlap:
         - Invert vx (horizontal speed) to make the ball bounce.
         - Move the ball just outside the paddle, so that it does not get "stuck"
           (overlapping again on the next frame and bouncing back and forth inside the paddle).
         - [OPTIONAL] You can also try to apply some "effect" making vy slightly dependent on where the ball
           hits the paddle (experiment!)

    Notes
    -----
    - The paddle and ball are both **axis-aligned**, so no trigonometry is needed.
    - The collision box ignores the ball's circular shape for simplicity,
      which is sufficient for this game.
    """
    # TODO: put your code!!!!
    hit = False # Per defecte suposem que no hi ha hagut una col·lisió.

    # 1. Definim les vores de la pilota com un rectangle amb centre a (x,y) i amb un radi "radius".
    ball_left = x - radius
    ball_right = x + radius
    ball_top = y - radius
    ball_bottom = y + radius

    # 2. Definim les vores de la pala com un rectangle amb cantonada superior esquerra a (paddle_x, paddle_y) i afamb amplada "paddle_w" i alçada "paddle_h".
    # Les dimensions no fan referencia a una pala en concret, sinó que a qualsevol pala. En la funció main() es cridarà dues vegades en cada bucle per definir cadascuna de les pales. 
    paddle_left = paddle_x  # Costat esquerre de la pala
    paddle_right = paddle_x + paddle_w  # Costat dret de la pala
    paddle_top = paddle_y   # Costat superior de la pala
    paddle_bottom = paddle_y + paddle_h # Costat inferior de la pala

    # 3. Comprovem si hi ha superposició entre la pilota i la pala (col·lisió).
    if (ball_right > paddle_left and ball_left < paddle_right and  ball_bottom > paddle_top and ball_top < paddle_bottom):
        # Comprovem  que el costat dret de la pilota és més gran que el costat esquerre de la pala, si és així hi ha hagut una colisió (pilota xoca a la pala pel seu costat esquerre)
        # Comprovem que el costat esquerre de la pilota és més petit que el costat dret de la pala, si és així hi ha hagut una colisió (pilota xoca a la pala pel sue costat dret)
        # Comprovem que el costat inferior de la pilota és més gran que el costat superior de la pala, si és així hi ha hagut una colisió (pilota xoca a la pala pel seu costat superior)
        # Comprovem que el costat superior de la pilota és més petit que el costat inferior de la pala, si és així hi ha hagut una colisió (pilota xoca a la pala pel seu costat inferior)
        hit = True # Afirmem que s'ha produït una col·lisió

    # 4. En cas de col·lisió, evitem la superposició de la pilota amb la pala actualitzant la seva posició en el moment del xoc. 
        if vx < 0: # Si vx amb la que es desplaça la pilota és negativa, indica que el xoc es produeix a la cara dreta de la pala (la pilota es desplaça cap a l'esquerra). 
            x = paddle_right + radius # La nova posició de la pilota és just fora de la pala, a la dreta (la vora esquerra de la pilota és a la vora dreta de la pala), evitant així que es superposin els dos elements. 

        else: # Si vx amb la que es desplaça la pilota és positiva, indica que el xoc es produeix a la cara esquerra de la pala (la pilota es desplaça cap a la dreta).
            x = paddle_left - radius # La nova posició de la pilota és just fora de la pala, a l'esquerra (la vora dreta de la pilota és a la vora esquerra de la pala), evitant així que es superposin els dos elements.

    # 5. Invertim la velocitat horitzontal de la pilota per generar el rebot. 
        vx = -vx # Invertim la velocitat horitzontal de la pilota per generar el revot (la pilota es desplaçara en sentit contrari en l'eix de les x)

    return x, y, vx, vy, hit

  

def reset_ball(center_x: int, center_y: int, vx0: int, vy0: int, to_right: bool) -> tuple[int, int, int, int]:
    """ Reset the ball to the center of the screen and return its initial position and velocity after a point has been scored.

    The ball should always restart from the center coordinates given by `center_x` and `center_y`, 
    but its horizontal direction depends on the Boolean parameter `to_right`:
      - If `to_right` is True  → the ball moves to the right.
      - If `to_right` is False → the ball moves to the left.

    A small random variation may be added to the vertical speed so that the game does not become too predictable.

    Parameters
    ----------
    center_x : int  - The x-coordinate of the screen center (starting horizontal position).
    center_y : int  - The y-coordinate of the screen center (starting vertical position).
    vx0 : int       - The base horizontal speed to be used (positive number).
    vy0 : int       - The base vertical speed to be used (positive number).
    to_right : bool - True if the ball should start moving to the right, False for the left.

    Returns
    -------
    x, y, vx, vy:
        x  new horizontal position (center)
        y  new vertical position (center)
        vx horizontal velocity (sign depends on `to_right`)
        vy vertical velocity (possibly randomized sign and/or magnitude)

    Notes and hints
    ---------------
    - The function should not draw anything, only compute and return values.
    - The starting position is always the screen center.
    - The horizontal velocity must point in the correct direction depending on `to_right`.
    - Optionally, randomize the vertical velocity slightly (e.g., sign or magnitude) for variability.
    """

    # TODO: put your code!!!!

    # 1. Assignem les coordenades centrals de la pilota
    x = center_x
    y = center_y

    # 2. Assignem la velocitat horitzontal segons la direcció en funció del paràmetre bool "to right".
    if to_right == True: 
        vx = vx0  # Si to_right és True, la velocitat horitzontal és positiva (cap a la dreta)
    else:
        vx = -vx0  # Si to_right és False, la velocitat horitzontal és negativa (cap a l'esquerra)

    # 3. Assignem la velocitat vertical amb una variació aleatòria (apartat opcional).
    variation = 1   # La màxima variació que es pot afegir o restar serà de +-1 respecte vy0
    vy = random.randint(vy0 - variation, vy0 + variation)    # La velocitat vertical serà un valor aleatori qualsevol entre vy0-1 i vy0+1

    if vy < 1: 
        vy = 1  # Si la velocitat vertical és negativa o 0, la fem positiva per assegurar que la pilota no es mourà en línia recta. 

    if random.randint(0, 1) == 0:  # El sentit es decideix amb un 50% de probabilitat de ser cap amunt o cap avall.
        vy = -vy  # Si el valor aleatori és 0, invertim el signe de la velocitat vertical per fer que la pilota es mogui cap amunt.

    # Es retorna la posició inicial de la pilota (x, y) i les velocitats (vx, vy) després de reiniciar-la al centre de la pantalla.
    return x, y, vx, vy



def compute_ai_direction(ball_y: int, paddle_y: int, paddle_h: int) -> int:
    """ Compute the movement direction (-1, 0, +1) for an AI-controlled paddle.
    The goal is to make the paddle follow the ball vertically with a simple,
    limited reaction. The AI should move the paddle upward, downward,
    or stay still depending on the position of the ball relative to the
    paddle's center.

    Parameters
    ----------
    ball_y : int
        The current vertical position of the ball (center of the ball).
    paddle_y : int
        The current vertical position of the paddle (top edge).
    paddle_h : int
        The height of the paddle (to compute its center).

    Returns
    -------
    int
        -1 → move up  
         0 → stay still  
        +1 → move down
    
    Notes and hints
    ---------------
    The function should return only the direction, not update positions.
    You might want to use a small tolerance margin so the paddle doesn't “vibrate” 
    when the ball is aligned enough.
    """
    # TODO: put your code!!!!

    # This line of code has been left for letting the full program work
    # You will need to eliminate it when adding your code
    return 0

# =============================================
# Checking KEYS UP/DOWN (given to the students)
# =============================================

def read_player_direction(keys, key_up: int, key_down: int) -> int:
    """Return -1, 0, or +1 based on pressed keys."""
    if keys[key_up]:
        return -1
    elif keys[key_down]:
        return 1
    return 0

# =================================
# Rendering (given to the students)
# =================================

def draw_scene(screen: pygame.Surface,
               x: int, y: int,
               p1y: int, p2y: int,
               score_left: int, score_right: int,
               paddle_h: int, ball_radius: int,
               backg_col, foreg_col) -> None:
    
    screen.fill(backg_col)
    # center line
    pygame.draw.line(screen, foreg_col, (WIDTH//2, 0), (WIDTH//2, HEIGHT), 1)
    # paddles
    pygame.draw.rect(screen, foreg_col, pygame.Rect(PADDLE_MARGIN, int(p1y), PADDLE_W, paddle_h))
    pygame.draw.rect(screen, foreg_col, pygame.Rect(WIDTH - PADDLE_MARGIN - PADDLE_W, int(p2y), PADDLE_W, paddle_h))
    # ball
    pygame.draw.circle(screen, foreg_col, (int(x), int(y)), ball_radius)
    # score (simple)
    font = pygame.font.Font(None, 48)
    text = font.render(f"{score_left}   {score_right}", True, foreg_col)
    rect = text.get_rect(center=(WIDTH//2, 40))
    screen.blit(text, rect)
    pygame.display.flip()

def show_message(screen: pygame.Surface,message: str,backg_col, foreg_col, show_time_ms) -> None:
    """Display 'message' centered on the game screen.
    Used at the end of the game"""
    # Choose font and text color
    font = pygame.font.Font(None, 96)     # default pygame font, size 96
    text = font.render(message, True, foreg_col)

    # Center the text in the middle of the screen
    rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))

    # Fill the screen with the background color and draw the text
    screen.fill(backg_col)
    screen.blit(text, rect)
    pygame.display.flip()

    # Pause for show_time_ms milliseconds so players can see it
    pygame.time.wait(show_time_ms)



# =================================
# Main loop (given to the students)
# =================================

def main() -> None:
    paddle_h, paddle_speed, speed_ball_x, speed_ball_y, ball_radius = get_config()
    backg_col, foreg_col = change_colors()

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Lab 2 - Pong")
    clock = pygame.time.Clock()

    # Initial state (no lists or objects)
    p1_y = (HEIGHT - paddle_h) / 2
    p2_y = (HEIGHT - paddle_h) / 2
    ball_x, ball_y, ball_vx, ball_vy = reset_ball(WIDTH//2, HEIGHT//2, speed_ball_x, speed_ball_y, to_right=True)

    score_left = 0
    score_right = 0

    running = True

    while running:
        # 1) Events (close window + input)
        direction_left = 0
        direction_right = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        keys = pygame.key.get_pressed()

        # Left paddle always human
        direction_left = read_player_direction(keys, KEY_UP_LEFT, KEY_DOWN_LEFT)

        # Right paddle can be human or AI
        if PLAY_AGAINST_MACHINE:
            direction_right = compute_ai_direction(ball_y, p2_y, paddle_h)
        else:
            direction_right = read_player_direction(keys, KEY_UP_RIGHT, KEY_DOWN_RIGHT)


        # 2) Update state (ONLY by calling functions)
        p1_y = move_paddle(p1_y, direction_left, paddle_speed, HEIGHT, paddle_h)
        p2_y = move_paddle(p2_y, direction_right, paddle_speed, HEIGHT, paddle_h)

        ball_x, ball_y = move_ball(ball_x, ball_y, ball_vx, ball_vy)
        ball_x, ball_y, ball_vx, ball_vy = collide_ball_walls(ball_x, ball_y, ball_vx, ball_vy, ball_radius, WIDTH, HEIGHT)

        # Collision with left paddle
        ball_x, ball_y, vx_tmp, vy_tmp, hit_left = collide_ball_paddle(
            ball_x, ball_y, ball_vx, ball_vy,
            PADDLE_MARGIN, p1_y, PADDLE_W, paddle_h, ball_radius
        )
        if hit_left:
            ball_vx, ball_vy = vx_tmp, vy_tmp

        # Collision with right paddle
        ball_x, ball_y, vx_tmp, vy_tmp, hit_right = collide_ball_paddle(
            ball_x, ball_y, ball_vx, ball_vy,
            WIDTH - PADDLE_MARGIN - PADDLE_W, p2_y, PADDLE_W, paddle_h, ball_radius
        )
        if hit_right:
            ball_vx, ball_vy = vx_tmp, vy_tmp

        # 3) Scoring (if ball leaves screen): reset ball
        if ball_x < -ball_radius:
            score_right += 1
            pygame.time.wait(SERVE_PAUSE)  # short pause before re-serve
            ball_x, ball_y, ball_vx, ball_vy = reset_ball(WIDTH//2, HEIGHT//2, speed_ball_x, speed_ball_y, to_right=True)
        elif ball_x > WIDTH + ball_radius:
            score_left += 1
            pygame.time.wait(SERVE_PAUSE)  # short pause before re-serve
            ball_x, ball_y, ball_vx, ball_vy = reset_ball(WIDTH//2, HEIGHT//2, speed_ball_x, speed_ball_y, to_right=False)
        
        if score_left == POINTS_END or score_right == POINTS_END:
            show_message(screen,"Game Over!",backg_col, foreg_col,2000)
            running = False

        # 4) Render
        draw_scene(screen, ball_x, ball_y, p1_y, p2_y, score_left, score_right, 
                   paddle_h, ball_radius, backg_col, foreg_col)

        clock.tick(FPS)

    # exiting the main loop
    pygame.quit()
    sys.exit(0)   # Ensures complete and clean exit from the program (avoids hanging processes)

# ADVANCED NOTE:   
# The following 2 lines, start the program by calling the main() function
# When you run: python pong.py, Python sets a built-in variable: __name__ = "__main__"
# So the condition is to make sure that this main() function runs only when you execute this file directly, 
# and not when it is imported from another file.
if __name__ == "__main__":
    main()