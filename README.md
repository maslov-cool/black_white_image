# black_white_image
Задание из Яндекс Лицея. Используя numpy, без питоновских циклов сконвертируйте цветное изображение в чёрно-белое.
По формуле:

 C = 0.2989 * R + 0.5870 * G + 0.1140 * B

 Считается, что вычисленный таким образом цвет лучше всего подходит для человеческого глаза, поскольку яркость каждой компоненты глаз воспринимает по-разному.
Напишите функцию bw_convert(), в которой проведите все необходимые операции.

Формат ввода
В папке с вашим решением будет лежать файл image.jpg c исходной картинкой.
Формат вывода
Результат сохраните в файл res.jpg в текущей папке.
Примечания
Не забудьте, что значение каждой составляющей цвета — целое число, поэтому результат необходимо округлить.
Для этого воспользуйтесь методом round() из библиотеки numpy.
Будем использовать формат изображения RGB.
