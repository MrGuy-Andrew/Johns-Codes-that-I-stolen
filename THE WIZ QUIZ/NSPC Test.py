import pygame

# Define the deadzone threshold
DEADZONE_THRESHOLD = 0.2

def handle_controller_input():
    # Initialize pygame
    pygame.init()

    # Initialize the controller module
    pygame.joystick.init()

    # Check the number of connected joysticks/controllers
    joystick_count = pygame.joystick.get_count()
    if joystick_count < 1:
        print("No controller connected.")
        pygame.quit()
        return

    # Get the first connected joystick/controller
    controller = pygame.joystick.Joystick(0)
    controller.init()

    # Print the name of the controller
    print("Controller Name:", controller.get_name())

    # Main loop
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Handle controller input events
            if event.type == pygame.JOYAXISMOTION:
                # Handle analog stick movements
                if event.axis == 0:
                    # X-axis of left analog stick
                    x_axis = event.value
                    # Apply deadzone
                    if abs(x_axis) < DEADZONE_THRESHOLD:
                        x_axis = 0.0
                    # Print only if there is input
                    if x_axis != 0.0:
                        print("X-axis:", x_axis)
                elif event.axis == 1:
                    # Y-axis of left analog stick
                    y_axis = event.value
                    # Apply deadzone
                    if abs(y_axis) < DEADZONE_THRESHOLD:
                        y_axis = 0.0
                    # Print only if there is input
                    if y_axis != 0.0:
                        print("Y-axis:", y_axis)
                # Add more conditions to handle other axes, if needed

            elif event.type == pygame.JOYBUTTONDOWN:
                # Handle button press events
                if event.button == 0:
                    # A button
                    # Perform actions when A button is pressed
                    # Add your own logic here
                    print("A button pressed")
                elif event.button == 1:
                    # B button
                    # Perform actions when B button is pressed
                    # Add your own logic here
                    print("B button pressed")
                # Add more conditions to handle other buttons, if needed

    # Quit the program
    pygame.quit()

# Call the function to handle controller input
handle_controller_input()
