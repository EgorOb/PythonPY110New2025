from django.shortcuts import render
from django.http import HttpResponse
import random
from django.views.decorators.csrf import csrf_exempt


def load_products_html(request):  # Возвращаем список продуктов через html
    products = ["Телефон", "Ноутбук", "Наушники", "Клавиатура", "Мышь", "Монитор"]
    html = "".join(f"<li>{product}</li>" for product in
                   random.sample(products, 4))  # Получаем 4 случайных товара из списка и формируем html
    return HttpResponse(html)


def load_products_with_render(request):  # Возвращаем список продуктов через render шаблона list_products.html
    products = ["Телефон", "Ноутбук", "Наушники", "Клавиатура", "Мышь", "Монитор"]
    return render(request, 'app_htmx/list_products.html', {'products': random.sample(products, 4)})


def product_list_view(request):  # Основной шаблон с кнопкой перезагрузки продуктов
    return render(request, 'app_htmx/products.html')


# ____________ представления для demo_hx_target
def hx_target_view(request):
    return render(request, 'app_htmx/demo_hx_target.html')


def load_status(request):
    return HttpResponse('<button disabled>Статус: OK</button>')


def row_details(request):
    return HttpResponse("""
    <tr>
        <td colspan="3">Подробности: Товар A, Цена: 100₽</td>
    </tr>
    """)


def product_details(request):
    return HttpResponse("Описание: Это классный товар!")


def more_info(request):
    return HttpResponse("Дополнительная информация загружена.")


@csrf_exempt
def validate_email(request):
    email = request.POST.get("email", "")
    if "@" not in email:
        return HttpResponse("<span style='color: red'>Ошибка: Некорректный email</span>")
    return HttpResponse("<span style='color: green'>Email корректен!</span>")


def get_result(request):
    return HttpResponse("Результат обновлён!")


def show_note(request):
    return HttpResponse("Новое сообщение: добро пожаловать!")


# __________ представления для demo_hx_swap

def hx_swap_view(request):
    return render(request, 'app_htmx/demo_hx_swap.html')


def swap_inner(request):
    return HttpResponse("<b>Заменённый innerHTML</b>")


def swap_outer(request):
    return HttpResponse("<div class='response' id='outer' style='color: red; background: #7abaff;'>Полностью заменён outerHTML</div>")


def swap_text(request):
    return HttpResponse("<b>Это будет видно как текст, а не HTML</b>")


def swap_before(request):
    return HttpResponse("<div style='color: green;'>→ ДО элемента</div>")


def swap_after_begin(request):
    return HttpResponse("<div style='color: blue;'>⇨ ВСТАВКА В НАЧАЛО</div>")


def swap_before_end(request):
    return HttpResponse("<div style='color: purple;'>⇦ ВСТАВКА В КОНЕЦ</div>")


def swap_after(request):
    return HttpResponse("<div style='color: orange;'>→ ПОСЛЕ элемента</div>")


def swap_delete(request):
    return HttpResponse("")  # HTMX просто удалит элемент


def swap_none(request):
    # Код выполнится
    return HttpResponse("<div style='color: gray;'>Этот ответ не будет вставлен</div>")