require 'test_helper'

class WeatherControllerTest < ActionDispatch::IntegrationTest
  test "should get index" do
    get weather_index_url
    assert_response :success
  end

  test "should get predict" do
    get weather_predict_url
    assert_response :success
  end

  test "should get display" do
    get weather_display_url
    assert_response :success
  end

end
