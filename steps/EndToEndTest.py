import time
from decimal import Decimal

from behave import *
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


class EndToEndTest:

    @given(u'I have Logged In and I am on the Home Page')
    def step_impl(context):
        # time.sleep(5)
        wait = WebDriverWait(context.driver, timeout=25, poll_frequency=1, ignored_exceptions=None)

        context.driver.get("https://magento.softwaretestingboard.com/")
        context.driver.find_element(By.LINK_TEXT, 'Sign In').click()

        email = wait.until(EC.presence_of_element_located((By.ID, 'email')))
        email.send_keys("dono@gmail.com")

        # context.driver.find_element(By.ID, 'email').send_keys("dono@gmail.com")

        password = wait.until(EC.presence_of_element_located((By.ID, 'pass')))
        password.send_keys("donodono12!")

        # context.driver.find_element(By.ID, 'pass').send_keys("donodono12!")

        sendbutton = wait.until(EC.presence_of_element_located((By.ID, 'send2')))
        sendbutton.click()

        # context.driver.find_element(By.ID, 'send2').click()

        element = wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Welcome, dono kasino!')]")))

        assert "Welcome" in element.text


    @when(u'I Click Shop New Yoga button')
    def step_impl(context):
        wait = WebDriverWait(context.driver, timeout=25, poll_frequency=1, ignored_exceptions=None)

        element = wait.until(EC.presence_of_element_located((By.XPATH, "//span[@class='action more button']")))
        element.click()


    @then(u'Page Title Heading the collection appears')
    def step_impl(context):
        wait = WebDriverWait(context.driver, timeout=25, poll_frequency=1, ignored_exceptions=None)

        # 1. Get the title page with a name of the collection
        element = wait.until(EC.presence_of_element_located((By.XPATH, "//span[@data-ui-id='page-title-wrapper' and text()='New Luma Yoga Collection']")))

        # 2. Check and Makesure the collection title name on the page and title window is same
        assert element.text == "New Luma Yoga Collection"
        assert context.driver.title == "New Luma Yoga Collection"


    @then(u'There are items on the page have at least 1 item or more')
    def step_impl(context):
        wait = WebDriverWait(context.driver, timeout=25, poll_frequency=1, ignored_exceptions=None)

        # 1. Get each toolbar amount
        elementToolbarAmount = wait.until(EC.presence_of_element_located((By.ID, "toolbar-amount")))
        elementsToolbarNumber = elementToolbarAmount.find_elements(By.CLASS_NAME, "toolbar-number")

        # 2. Then check and makesure there are no 0 value
        for element in elementsToolbarNumber:
            print(element.text)
            assert element.text != "0"


    @when(u'I Click an Item on Product List')
    def step_impl(context):

        wait = WebDriverWait(context.driver, timeout=25, poll_frequency=1, ignored_exceptions=None)

        # 1. Get Element Products and assign the first product
        elementProductGrid = wait.until(EC.presence_of_element_located((By.XPATH, "//ol[@class='products list items product-items']")))
        elementsProduct = elementProductGrid.find_elements(By.XPATH, "//li[@class='item product product-item']")
        firstProduct = elementsProduct[0]

        # 2. Get the product title and price, then sent to Global context
        elementProductTitle = firstProduct.find_element(By.CLASS_NAME, "product-item-link")
        elementProductPrice = firstProduct.find_element(By.CLASS_NAME, "price")
        context.productName = elementProductTitle.text
        context.productPrice = elementProductPrice.text

        # 3. Scroll/Move to the price element
        action = ActionChains(context.driver)
        action.move_to_element(elementProductPrice)
        action.perform()

        # 4. Click the product
        firstProduct.click()


    @then(u'Detail Page about the Product appears')
    def step_impl(context):
        wait = WebDriverWait(context.driver, timeout=25, poll_frequency=1, ignored_exceptions=None)

        # 1. Get product title and price element
        elementProductTitle = wait.until(EC.presence_of_element_located((By.XPATH, "//span[@itemprop='name']")))
        elementProductPrice = wait.until(EC.presence_of_element_located((By.XPATH, "//span[@data-price-type='finalPrice']")))
        # 2. Makesure the title and the price of the product is consistent
        assert elementProductTitle.text == context.productName
        assert elementProductPrice.text == context.productPrice


    @then(u'I Makesure the Product In Stock')
    def step_impl(context):
        wait = WebDriverWait(context.driver, timeout=25, poll_frequency=1, ignored_exceptions=None)

        # Get Stock element on the web page, then makesure is In stock
        elementStock = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@title='Availability']")))
        assert elementStock.text == "IN STOCK"


    @when(u'I Choose Size, Color, and Quantity the Product')
    def step_impl(context):
        wait = WebDriverWait(context.driver, timeout=25, poll_frequency=1, ignored_exceptions=None)

        # Choose Size
        # 1. Size Option, Get the grid size option then get all element size option
        elementSizeDiv = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@attribute-code='size']")))
        elementsSizeOption = elementSizeDiv.find_elements(By.XPATH, "//div[@class='swatch-option text']")
        assert len(elementsSizeOption) != 0
        # 2. Get the first option size of the product, then click the option
        firstSizeOption = elementsSizeOption[0]
        firstSizeOption.click()
        # 3. Add selected option SIZE to Global context
        context.productSize = firstSizeOption.text
        # time.sleep(5)

        # Choose Color
        # 1. Color Option, Get the grid color option then get all element color option
        elementColorDiv = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@attribute-code='color']")))
        elementsColorOption = elementColorDiv.find_elements(By.XPATH, "//div[@class='swatch-option color']")
        assert len(elementsColorOption) != 0
        # 2. Get the first option color of the product. then click the option
        firstColorOption = elementsColorOption[0]
        firstColorOption.click()
        # 3. Add selected option COLOR to Global context
        context.productColor = firstColorOption.get_attribute("option-label")
        # time.sleep(5)

        # Quantity
        # 1. Get Quantity element and move to the element until visible on screen
        elementQuantity = wait.until(EC.presence_of_element_located((By.ID, "qty")))
        action = ActionChains(context.driver)
        action.move_to_element(elementQuantity)
        action.perform()
        # 2. Clear Quantity input then input 1
        elementQuantity.clear()
        elementQuantity.send_keys("1")


    @when(u'I Click Add to Cart button')
    def step_impl(context):
        wait = WebDriverWait(context.driver, timeout=25, poll_frequency=1, ignored_exceptions=None)

        # Search element and Click Add to Cart button
        elementAddToCartBtn = wait.until(EC.presence_of_element_located((By.ID, "product-addtocart-button")))
        elementAddToCartBtn.click()

    @then(u'The Product Success Added to Shopping Cart')
    def step_impl(context):
        wait = WebDriverWait(context.driver, timeout=25, poll_frequency=1, ignored_exceptions=None)

        # Search success alert element and Check the success message
        elementAlert = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@data-ui-id='message-success']")))
        assert elementAlert.text == "You added " + context.productName + " to your shopping cart."

    @when(u'I Go to the Shopping Cart')
    def step_impl(context):
        wait = WebDriverWait(context.driver, timeout=25, poll_frequency=1, ignored_exceptions=None)


        # SHOPPING CART
        # 1. Get Shopping cart element, click the element then Assert to makesure dropdowndialog shopping cart showup
        elementShoppingCart = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@data-block='minicart']")))
        elementShoppingCart.click()
        cartClassName = elementShoppingCart.get_attribute("class")
        assert "active" in cartClassName


        # SHOPPING CART DROPDOWN DIALOG
        # 2. Get Dropdowndialog shopping cart as base element, then get Amount Item in Cart and get Cart Subtotal
        elementDropdownDialog = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@data-role='dropdownDialog']")))
        dropdownItemAmountInCart = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "items-total")))
        dropdownDialogSubTotal = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "price")))
        assert dropdownItemAmountInCart.text == "1 Item in Cart"
        assert dropdownDialogSubTotal.text == context.productPrice

        # 3. Get ProductItemDetail as base element from context elementDropdownDialog
        productItemDetail = WebDriverWait(elementDropdownDialog, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "product-item-details"))
        )


        # PRODUCT NAME, PRICE, QTY
        # 4. Use ProductItemDetail as context, then find Item/Product Name, Product Price, and Product Qty input
        productName = WebDriverWait(productItemDetail, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "product-item-name"))
        )
        productPrice = WebDriverWait(productItemDetail, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "price"))
        )
        productQty = WebDriverWait(productItemDetail, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "input"))
        )
        assert productName.text == context.productName
        assert productPrice.text == context.productPrice
        assert productQty.get_attribute("data-item-qty") == "1"


        # SEE DETAILS (Size and Color)
        # 5. Get See Details element on the Dialog, then click the Details and Assert should be showup
        elementSeeDetails = WebDriverWait(productItemDetail, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@role='tablist']"))
        )
        elementSeeDetails.click()
        detailTabActive = elementSeeDetails.get_attribute("class")
        assert "active" in detailTabActive

        # 6. Get Size and Color element then Assert to makesure the color and the size are consistent
        elementsValues = WebDriverWait(elementSeeDetails, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//dd[@class='values']"))
        )
        assert len(elementsValues) == 2 # ElementValue[0] = size, ElementValue[1] = color
        assert elementsValues[0].text == context.productSize
        assert elementsValues[1].text == context.productColor


        # VIEW AND EDIT
        # 7. Click View and Edit Cart and go to Shopping Cart Page
        elementViewAndEditCart = WebDriverWait(elementDropdownDialog, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "View and Edit Cart"))
        )
        elementViewAndEditCart.click()


    @then(u'Shopping Cart Page appears')
    def step_impl(context):
        wait = WebDriverWait(context.driver, timeout=25, poll_frequency=1, ignored_exceptions=None)

        # Get title page and then Makesure the title page is Shopping Cart
        element = wait.until(EC.presence_of_element_located((By.XPATH, "//span[@data-ui-id='page-title-wrapper' and text()='Shopping Cart']")))
        assert context.driver.title == "Shopping Cart"
        assert element.text == "Shopping Cart"

    @then(u'I Verify the Product data is Valid')
    def step_impl(context):
        wait = WebDriverWait(context.driver, timeout=25, poll_frequency=1, ignored_exceptions=None)

        # TABLE Data Product
        # 1. Get table data as BASE finding
        elementShoppingCartTables = wait.until(EC.presence_of_element_located((By.ID, "shopping-cart-table")))


        # 2. Get Product Name and then Makesure the Product Name is consistent
        productName = WebDriverWait(elementShoppingCartTables, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "product-item-name"))
        )
        assert productName.text == context.productName

        # 3. Get Size and Color and then Makesure the Size and the Color are consistent
        itemOptions = WebDriverWait(elementShoppingCartTables, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "item-options"))
        )
        itemValues = WebDriverWait(itemOptions, 10).until(
            EC.presence_of_all_elements_located((By.TAG_NAME, "dd"))
        )
        assert len(itemValues) == 2 # itemValues[0] = size, itemValues[1] = color
        assert itemValues[0].text == context.productSize
        assert itemValues[1].text == context.productColor

        # 4 . Get Price, Get SubTotal, Get Quantity then Makesure the Price, Subtotal, and Quantity on the table are consistent
        productPriceTable = elementShoppingCartTables.find_element(By.XPATH, "//td[@data-th='Price']")
        productSubTotalTable = elementShoppingCartTables.find_element(By.XPATH, "//td[@data-th='Subtotal']")
        productQtyTable = elementShoppingCartTables.find_element(By.TAG_NAME, "input")
        assert productPriceTable.text == context.productPrice
        assert productSubTotalTable.text == context.productPrice
        assert productQtyTable.get_attribute("value") == "1"


        # SUMMARY Data Product
        # 5. Click Estimate Shipping and Tax then Makesure the detail Shipping and Tax appears
        estimateShippingTax = wait.until(EC.presence_of_element_located((By.ID, "block-shipping")))
        estimateShippingTax.click()
        estimateShippingClass = estimateShippingTax.get_attribute("class")
        assert "active" in estimateShippingClass

        # 6. Select Country
        elementSelectCountry = wait.until(EC.presence_of_element_located((By.NAME, "country_id")))
        elementSelectCountry.click()
        selectDropdown = Select(elementSelectCountry)
        # values = selectDropdown.options
        selectDropdown.select_by_value("ID")

        # 7. Input State/Province
        elementProvince = wait.until(EC.presence_of_element_located((By.NAME, "region")))
        elementProvince.clear()
        elementProvince.send_keys("Jakarta")

        # 8. Input ZIP/Postal Code
        elementPostalCode = wait.until(EC.presence_of_element_located((By.NAME, "postcode")))
        elementPostalCode.clear()
        elementPostalCode.send_keys("11440")

        # 9. Click RadioButton FlatRate Shipping
        elementRadioFlatRate = wait.until(EC.presence_of_element_located((By.ID, "s_method_flatrate_flatrate")))
        action = ActionChains(context.driver)
        action.move_to_element(elementRadioFlatRate)
        action.perform()
        elementRadioFlatRate.click()

        # 10. Get Shipping FlatRate Price
        time.sleep(6) # Wait 6 Sec (Loading)
        elementFieldChoiceItem = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='field choice item']")))
        elementPriceFlatRate = elementFieldChoiceItem.find_element(By.CLASS_NAME, 'price')
        splitString = elementPriceFlatRate.text
        flatRateValue = Decimal(splitString.split('$')[1]) # Get dollar value
        context.shippingPriceFlatRate = flatRateValue


        # ElementCartTotals as BASE
        elementCartTotals = wait.until(EC.presence_of_element_located((By.ID, "cart-totals")))
        # Element TotalsSub as CHILD BASE
        elementTotalsSub = WebDriverWait(elementCartTotals, 10).until(
            EC.presence_of_element_located((By.XPATH, "//tr[@class='totals sub']"))
        )

        # 11. Get Subtotal Price from SUMMARY
        elementPriceSubtotal = WebDriverWait(elementTotalsSub, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@data-th='Subtotal']"))
        )
        elementTotalShipping = WebDriverWait(elementCartTotals, 10).until(
            EC.presence_of_element_located((By.XPATH, "//tr[@class='totals shipping excl']"))
        )
        # 12. Get Shipping Price from SUMMARY
        elementPriceWithShipping = WebDriverWait(elementTotalShipping, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@data-th='Shipping']"))
        )

        # Grand Totals as BASE
        elementGrandTotals = wait.until(EC.presence_of_element_located((By.XPATH, "//tr[@class='grand totals']")))
        # 13. Get Order Total Price from SUMMARY
        elementOrderTotal = WebDriverWait(elementGrandTotals, 10).until(
            EC.presence_of_element_located((By.XPATH, "//td[@data-th='Order Total']"))
        )

        print("------------------------------------------------------")
        print("elementPriceSubtotal : " + elementPriceSubtotal.text)
        print("price with shipping : " + elementPriceWithShipping.text)
        print("Order total : ", elementOrderTotal.text)

        splitPriceSubtotal = elementPriceSubtotal.text
        priceSubtotal = Decimal(splitPriceSubtotal.split('$')[1]) # Get dollar value
        splitPriceShipping = elementPriceWithShipping.text
        priceShipping = Decimal(splitPriceShipping.split("$")[1]) # Get dollar value
        splitOrdertotal = elementOrderTotal.text
        orderTotal = Decimal(splitOrdertotal.split("$")[1]) # Get dollar value
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~c")
        print(priceSubtotal)
        print(priceShipping)
        print(orderTotal)
        
        assert priceShipping == context.shippingPriceFlatRate
        assert (priceSubtotal+priceShipping) == orderTotal

    @when(u'I Click Proceed to Checkout button')
    def step_impl(context):
        wait = WebDriverWait(context.driver, timeout=25, poll_frequency=1, ignored_exceptions=None)

        # Click Checkout Button
        elementBtnCheckout = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@data-role='proceed-to-checkout']")))
        elementBtnCheckout.click()

    @then(u'Shipping Address appears')
    def step_impl(context):
        wait = WebDriverWait(context.driver, timeout=25, poll_frequency=1, ignored_exceptions=None)
        try:
            wait.until(EC.invisibility_of_element_located((By.ID, "checkout-loader")))
        except:
            print("Time out")

        # Base ShippingAdress
        baseShippingAddress = wait.until(EC.presence_of_element_located((By.ID, "shipping")))
        # Get Element Title then Makesure there is title on the page "Shipping Adress"
        elementTitle = WebDriverWait(baseShippingAddress, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "step-title"))
        )
        assert elementTitle.text == "Shipping Address"
        assert context.driver.title == "Checkout"

    @then(u'I Verify the Product from Order Summary is Valid')
    def step_impl(context):
        wait = WebDriverWait(context.driver, timeout=25, poll_frequency=1, ignored_exceptions=None)

        # Block Order Summary as BASE
        baseBlockSummary = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "opc-block-summary")))

        # 1. Verify and makesure the Item Count in Order Summary is 1
        elementItemCount = WebDriverWait(baseBlockSummary, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@data-bind='text: getCartSummaryItemsCount()']"))
        )
        # Debug
        print("---------1.Verify and makesure the Item Count in Order Summary is 1------")
        print("elementItemCount : " + elementItemCount.text)
        assert elementItemCount.text == "1"

        # 2. Click Item In Cart then makesure the ItemCart is active
        elementItemInCart = WebDriverWait(baseBlockSummary, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='block items-in-cart']"))
        )
        elementItemInCart.click()
        time.sleep(10)
        # Debug
        print("---------2.Click Item In Cart then makesure the ItemCart is active------")
        print("class now : " + elementItemInCart.get_attribute("class"))
        assert "active" in elementItemInCart.get_attribute("class")


        # Product Item Detail as BASE CHILD (Block Order Summary)
        baseProductItemDetails = WebDriverWait(baseBlockSummary, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "product-item-details"))
        )

        # 3. Verify Product Item Name is consistent
        elementProductItemName = WebDriverWait(baseProductItemDetails, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "product-item-name"))
        )
        # Debug
        print("---------3.Verify Product Item Name is consistent------")
        print("elementProductItemName : " + elementProductItemName.text)
        print("context.productName : " + context.productName)
        assert elementProductItemName.text == context.productName

        # 4. Verify Product Quantity is 1
        elementProductQty = WebDriverWait(baseProductItemDetails, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "value"))
        )
        # Debug
        print("---------4.Verify Product Quantity is 1------")
        print("elementProductQty : " + elementProductQty.text)
        assert elementProductQty.text == "1"

        # 5. Verify Product Price is consistent
        elementProductPrice = WebDriverWait(baseProductItemDetails, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "price"))
        )
        # Debug
        print("---------5.Verify Product Price is consistent------")
        print("elementProductPrice : " + elementProductPrice.text)
        print("context.productPrice : " + context.productPrice)
        assert elementProductPrice.text == context.productPrice

        # 6. Click View Details toggle and makesure the view details toggle is active
        elementViewDetails = WebDriverWait(baseProductItemDetails, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "toggle"))
        )
        elementViewDetails.click()
        # Debug
        print("---------6.Click View Details toggle and makesure the view details toggle is active------")
        print("aria-selected : " + elementViewDetails.get_attribute("aria-selected"))
        print("aria-expanded : " + elementViewDetails.get_attribute("aria-expanded"))
        assert elementViewDetails.get_attribute("aria-selected") == "true"
        assert elementViewDetails.get_attribute("aria-expanded") == "true"

        # 7. Verify the Product Size and the Product Color is consistent
        elementsValues = WebDriverWait(baseProductItemDetails, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "values"))
        )
        # Debug
        print("---------7.Verify the Product Size and the Product Color is consistent------")
        print("size: " + elementsValues[0].text)
        print("color: " + elementsValues[1].text)
        assert len(elementsValues) == 2 # elementValues[0] = size, elementValues[1] = color
        assert elementsValues[0].text == context.productSize # Size
        assert elementsValues[1].text == context.productColor # Color


    @when(u'I Click + New Address button')
    def step_impl(context):
        raise NotImplementedError(u'STEP: When I Click + New Address button')

    @then(u'Shipping Address Modal appears')
    def step_impl(context):
        raise NotImplementedError(u'STEP: Then Shipping Address Modal appears')

    @when(u'I Filled Shipping Address correctly')
    def step_impl(context):
        raise NotImplementedError(u'STEP: When I Filled Shipping Address correctly')

    @when(u'I Click Ship here button')
    def step_impl(context):
        raise NotImplementedError(u'STEP: When I Click Ship here button')

    @then(u'The New Added Address show up')
    def step_impl(context):
        raise NotImplementedError(u'STEP: Then The New Added Address show up')

    @when(u'I Choose Shipping Methods')
    def step_impl(context):
        raise NotImplementedError(u'STEP: When I Choose Shipping Methods')

    @when(u'I Click Next button')
    def step_impl(context):
        raise NotImplementedError(u'STEP: When I Click Next button')

    @then(u'Payment Method appears')
    def step_impl(context):
        raise NotImplementedError(u'STEP: Then Payment Method appears')

    @then(u'I Verify the Order Summary and the Address')
    def step_impl(context):
        raise NotImplementedError(u'STEP: Then I Verify the Order Summary and the Address')

    @when(u'I Check my billing and shipping address are the same')
    def step_impl(context):
        raise NotImplementedError(u'STEP: When I Check my billing and shipping address are the same')

    @when(u'I Click Place Order button')
    def step_impl(context):
        raise NotImplementedError(u'STEP: When I Click Place Order button')

    @then(u'The Order should be successful')
    def step_impl(context):
        raise NotImplementedError(u'STEP: Then The Order should be successful')