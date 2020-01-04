"""
Moduł zawierąjący funkcje main. Jest to moduł wykonawczy
"""
import files
import function
import modules
import pythonfiles
import registration
import functions


def main():
    """Funkcja wykonująca cały program"""
    modul = modules.Modules()
    fun = function.Functions()
    file = files.Files()
    register = registration.Registration()

    files_with_code = pythonfiles.FileInDirectory()
    path = r'.\\'
    extend = 'py'
    result = files_with_code.list_directory(path, extend)

    files.Files.checking_connections_between_files(result)

    function_list1 = function.Functions.checking_connections_between_functions1(result)
    function_list2 = fun.checking_weight_of_connections_between_functions(result, function_list1)
    weight_fun = functions.write_to_file_fun_data(function_list1, function_list2)
    function.Functions.checking_connections_between_functions(result, weight_fun)

    modul_list = modules.Modules.searching_for_used_modules(result)
    modules.Modules.checking_connections_between_modules(result, modul_list)

    menu_choice = functions.menu()

    if menu_choice == 1:
        registration.Registration.write_to_file("FILES",
                                                files.Files.filesConnectionList)  # Wpisywanie do pliku połączeń plików
        registration.Registration.write_to_file("", files.Files.filesConnectionWeight)

        functions.cyclomatic_complexity()

    elif menu_choice == 2:
        registration.Registration.write_to_file("Functions",
                                                function.Functions.functionsConnectionList)  # Wpisywanie do pliku połączeń funkcji
        registration.Registration.write_to_file("", function.Functions.functionsConnectionWeight)

        functions.cyclomatic_complexity()

    elif menu_choice == 3:
        registration.Registration.write_to_file("Modules",
                                                modul.Modules.modulConnectionList)  # Wpisywanie do pliku połączeń modułów
        registration.Registration.write_to_file("", modul.Modules.modulConnectionWeight)

        functions.cyclomatic_complexity()

    elif menu_choice == 4:
        registration.Registration.write_to_file("FILES",
                                                files.Files.filesConnectionList)  # Wpisywanie do pliku połączeń plików
        registration.Registration.write_to_file("", files.Files.filesConnectionWeight)

        registration.Registration.write_to_file("Functions",
                                                function.Functions.functionsConnectionList)  # Wpisywanie do pliku połączeń funkcji
        registration.Registration.write_to_file("", function.Functions.functionsConnectionWeight)

        functions.cyclomatic_complexity()

    elif menu_choice == 5:
        registration.Registration.write_to_file("FILES",
                                                files.Files.filesConnectionList)  # Wpisywanie do pliku połączeń plików
        registration.Registration.write_to_file("", files.Files.filesConnectionWeight)

        registration.Registration.write_to_file("Modules",
                                                modules.Modules.modulConnectionList)  # Wpisywanie do pliku połączeń modułów
        registration.Registration.write_to_file("", modules.Modules.modulConnectionWeight)

        functions.cyclomatic_complexity()

    elif menu_choice == 6:
        registration.Registration.write_to_file("Functions",
                                                function.Functions.functionsConnectionList)  # Wpisywanie do pliku połączeń funkcji
        registration.Registration.write_to_file("", function.Functions.functionsConnectionWeight)

        registration.Registration.write_to_file("Modules",
                                                modules.Modules.modulConnectionList)  # Wpisywanie do pliku połączeń modułów
        registration.Registration.write_to_file("", modules.Modules.modulConnectionWeight)

        functions.cyclomatic_complexity()

    elif menu_choice == 7:
        registration.Registration.write_to_file("FILES",
                                                files.Files.filesConnectionList)  # Wpisywanie do pliku połączeń plików
        registration.Registration.write_to_file("", files.Files.filesConnectionWeight)

        registration.Registration.write_to_file("Functions",
                                                function.Functions.functionsConnectionList)  # Wpisywanie do pliku połączeń funkcji
        registration.Registration.write_to_file("", function.Functions.functionsConnectionWeight)

        registration.Registration.write_to_file("Modules",
                                                modules.Modules.modulConnectionList)  # Wpisywanie do pliku połączeń modułów
        registration.Registration.write_to_file("", modules.Modules.modulConnectionWeight)

        functions.cyclomatic_complexity()

    else:
        print("Wybrałeś opcję z poza zakresu")
        main()


main()
