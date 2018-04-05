import numpy as np

class CONSTANTS:

    # DISPLAY
    FPS = 10

    CAR_WIDTH = 0.66
    CAR_LENGTH = 1.33

    # ORIGIN
    AXES_SHOW = 0.5
    COORDINATE_SCALE = 150

    # POSITION BOUNDS
    Y_MINIMUM = 0
    Y_MAXIMUM = 1


    # OPTIMIZATION
    ACTION_TIMESTEPS = 100  # 5 seconds
    ACTION_TURNANGLE = 30  # degrees
    ACTION_NUMPOINTS = 100

    T_PAST = 10

    THETA_LIMITER_X = 0.01
    THETA_LIMITER_Y = 0.01

    LOSS_THRESHOLD = 0.01

    LEARNING_RATE = 0.1

    class PARAMETERSET_1:

        # DISPLAY
        SCREEN_WIDTH = 4
        SCREEN_HEIGHT = 5

        # SPEED
        VEHICLE_MAX_SPEED = 0.1

        # INITIAL CONDITIONS
        MACHINE_INITIAL_POSITION = np.array([-1, 0])

        # INTENTS
        HUMAN_INTENT = np.array([1, 1, -1])
        MACHINE_INTENT = np.array([0.001, 1, 0])

        # VEHICLE ORIENTATIONS
        HUMAN_ORIENTATION = 0
        MACHINE_ORIENTATION = 0

        # BOUNDS
        BOUND_HUMAN_X = None
        BOUND_HUMAN_Y = np.array([0, 1])

        BOUND_MACHINE_X = None
        BOUND_MACHINE_Y = np.array([0, 1])

        # LOSS WEIGHT
        Y_CLEARANCE_WEIGHT = 0.3

    class PARAMETERSET_2:

        # DISPLAY
        SCREEN_WIDTH = 5
        SCREEN_HEIGHT = 5

        # SPEED
        VEHICLE_MAX_SPEED = 0.1

        # INITIAL CONDITIONS
        MACHINE_INITIAL_POSITION = np.array([-2.5, 0])

        # INTENTS
        HUMAN_INTENT = np.array([1, 0, -1])
        MACHINE_INTENT = np.array([1, 1, 0])

        # VEHICLE ORIENTATIONS
        HUMAN_ORIENTATION = 90
        MACHINE_ORIENTATION = 0

        # BOUNDS
        BOUND_HUMAN_X = np.array([-0.4, 0.4])
        BOUND_HUMAN_Y = None

        BOUND_MACHINE_X = None
        BOUND_MACHINE_Y = np.array([-0.4, 0.4])

        # LOSS WEIGHT
        Y_CLEARANCE_WEIGHT = 1

class MATRICES:

    LOWER_TRIANGULAR_MATRIX = np.zeros((CONSTANTS.ACTION_NUMPOINTS, CONSTANTS.ACTION_NUMPOINTS))
    LOWER_TRIANGULAR_MATRIX[np.tril_indices(CONSTANTS.ACTION_NUMPOINTS, 0)] = 1




