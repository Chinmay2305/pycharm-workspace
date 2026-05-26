class Config:
    url = "http://qa.aerfinity.acumenaviation.in/"

    # LOGIN CONTROLS
    login_user_field = "input#email"
    login_pwd_field = "input#password"
    login_btn = "//button[contains(@class,'MuiButtonBase-root') and contains(@class,'MuiButton-containedPrimary') and contains(@class,'MuiButton-fullWidth')]"
    profile_img = "//div/div/div/img"  # for verifying successful login
    user = "support@acumen.aero"
    pwd = "Acumen@123"

    #FORGOT PASSWORD
    profile_icon = "//div/div/header/div/div/button"
    forgot_password_url = "https://qa.aerfinity.acumenaviation.in/forgot-password"
    forgot_password_field = "//div[2]/div/div/form/div/div/input"
    forgot_password_btn = "//div[2]/div/div/form/button" #"//div/form/button"

    #ADD ROLE
    settings = "//div/div/div/div/ul/a[7]"
    settings_role = "//div/main[1]/div/nav/ul/a[2]"
    add_role_btn = "//div[contains(@class,'MuiBox-root')])[9]/button[1]"
    add_role_name = "input#role_name"
    role_name = "Test Role"
    add_role_profile = "input#profile_type"
    profile_name = "User"
    role_save_btn = "//div[contains(@class,'MuiDialogActions-root')]/button[2]"
    role_cancel_btn = "//div[contains(@class,'MuiDialogActions-root')]/button[1]"