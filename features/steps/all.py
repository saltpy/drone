from selenium import webdriver

@when(u"I navigate to /")
def step_impl(context):
    context.driver = webdriver.Remote(
        command_executor="http://selenium:4444/wd/hub",
        desired_capabilities={"browserName": "chrome", "platform": "ANY", "version": ""}
    )


@then(u"I see the homepage")
def step_impl(context):
    context.driver.get("http://target:9000/")
