import flet as ft;

class User():
    def __init__(self):
        self.name = None;
        self.info = {
            "gender": None,
            "age": 0,  
            "height": 0,
            "weight": 0,
            "maintenance_calories": 0,
        };

    def fill_info(self, gender, age, height, weight):
        self.info["gender"] = gender;
        self.info["age"] = age;
        self.info["height"] = height;
        self.info["weight"] = weight;

    def get_maintenance_calories(self):
        if self.info["gender"] == "male":
            self.info["maintenance_calories"] = 66 + (6.2 * self.info["weight"]) + (12.7 * self.info["height"]) - (6.8 * self.info["age"])

        elif self.info["gender"] == "female":
            self.info["maintenance_calories"]= 655 + (4.35 * self.info["weight"]) + (4.7 * self.info["height"]) - (4.7 * self.info["age"])

        
class App():
    def __init__(self, page):
        self.page = page;
        self.user = None;

        self.create_user_control();
        
    def clear_controls(self):
        self.page.controls.clear();
        self.page.update();

    def refresh_page(self, fun):
        self.clear_controls();
        fun();

    def create_user_event(self, e):
        if self.name_textfield.value != "" and self.gender_dropdown.value != "" and self.age_textfield.value != "" and self.height_textfield.value != "" and self.weight_textfield.value != "": 
            self.user = User();
            self.user.fill_info(self.gender_dropdown.value, int(self.age_textfield.value), int(self.height_textfield.value), int(self.weight_textfield.value));
            self.user.get_maintenance_calories();
            self.refresh_page(self.create_dashboard_control);
        else:
            print("event")

            self.show_error("All fields are required");
    
    def show_error(self, err):
        self.page.open(
            ft.SnackBar(
                content = ft.Text(err),
                action = "OK",
            )
        )
        self.page.update();

  
    def create_user_control(self):
        self.name_textfield = ft.TextField(label = "Name");
        self.gender_dropdown = ft.Dropdown(label = "Gender", options = [
            ft.DropdownOption(key = "Male", content = ft.Text("Male")), 
            ft.DropdownOption(key = "Female", content = ft.Text("Female"))
        ]);
        self.age_textfield = ft.TextField(label = "Age");
        self.height_textfield = ft.TextField(label = "Height", hint_text="cm");
        self.weight_textfield = ft.TextField(label = "Weight", hint_text="lbs");

        self.page.add(
            ft.Column(
                controls = [
                    self.name_textfield,
                    self.gender_dropdown,
                    self.age_textfield,
                    self.height_textfield,
                    self.weight_textfield,
                    ft.Container(
                        content = ft.ElevatedButton(text="Submit", on_click = self.create_user_event),
                        alignment = ft.alignment.center,
                    ),
                ]
            )
        );

    def create_dashboard_control(self):
        pass;

def main(page: ft.Page):
    App(page);

ft.app(main);