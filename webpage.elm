import Browser
import Http
import Html exposing (..)
import Html.Attributes exposing (..)
import Html.Events exposing (..)
import Json.Decode exposing (Decoder, map2, field, string, int, bool)
import Dict



-- MAIN


main =
  Browser.element
    { init = init
    , update = update
    , view = view
    }



-- MODEL


type Model
  = Failure
  | Loading
  | Success String

type alias Bike =
  { number : Int
  , last_user : String
  , checkout_time : Int
  , needs_maintenance : Bool
  }


init : () -> (Model, Cmd Msg)
init _ =
  (Loading, getRandomCatGif)



-- UPDATE


type Msg
  = MorePlease
  | GotGif (Result Http.Error String)


update : Msg -> Model -> (Model, Cmd Msg)
update msg model =
  case msg of
    MorePlease ->
      (Loading, getRandomCatGif)

    GotGif result ->
      case result of
        Ok url ->
          (Success url, Cmd.none)

        Err _ ->
          (Failure, Cmd.none)


-- VIEW


view : Model -> Html Msg
view model =
  div []
    [ h2 [] [ text "Shrek is God" ]
    , viewGif model
    ]


viewGif : Model -> Html Msg
viewGif model =
  case model of
    Failure ->
      div []
        [ text "I could not load a bike for some reason. "
        , button [ onClick MorePlease ] [ text "Try Again!" ]
        ]

    Loading ->
      text "Loading..."

    Success url ->
      div []
        [ button [ onClick MorePlease, style "display" "block" ] [ text "More Please!" ]
        , img [ src url ] []
        ]



-- HTTP


getBikeData : Cmd Msg
getBikeData =
  Http.get
    { url = "http://127.0.0.1:5000/"
    , expect = Http.expectJson
    }


decoder : Decoder (Dict.Dict String Bike)
decoder =
  map (Dict.map infoToBike) (dict infoDecoder)

type alias Info =
  { number : Int
  , last_user : String
  , checkout_time : Int
  , needs_maintenance : Bool
  }

infoDecoder : Decoder Info
infoDecoder =
  map2 Bike
    (field "number" int)
    (field "last_user" string)
    (field "checkout_time" int)
    (field "needs_maintenance" bool)

infoToBike : String -> Info -> Bike
infoToBike number { last_user, checkout_time, needs_maintenance } =
  Bike number last_user checkout_time needs_maintenance
