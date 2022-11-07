class BigM:

    def validateUserInput(userInput: str) -> bool:
        """
        Checks whether the input provided by the user is well formatted or not
        Arguments:
            userInput : String
        Returns:
            True if :
                - User input follows the pattern: nx + ny + nz ( >= | <= | > | < | = ) n 
               Or
                - User input follows the pattern: (Max | Min) Z = nx + ny + nz
            False otherwise
        """
        pass

    def formatUserInput(userInput: list[str]) -> list[list[int]]:
        """
        The function takes an array of strings representing the input taken and **validated** from a jupyter user.
        The function returns a matrix.
        Arguments:
            userInput : array of string
        Returns:
            Matrix following the format shown in the output image bellow
        """