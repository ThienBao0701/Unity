using UnityEngine;
using UnityEngine.UI;
using TMPro;
using System.Collections.Generic;

public class MathDuelUI : MonoBehaviour
{
    Canvas canvas;
    TMP_Text question, timer, p1Score, p2Score, status;
    float timeLeft = 30f;
    int score1 = 0, score2 = 0;
    System.Random rng = new System.Random();

    Color Pink = new Color(1f, 0.46f, 0.72f);
    Color Purple = new Color(0.55f, 0.28f, 0.90f);
    Color Blue = new Color(0.25f, 0.55f, 0.95f);

    void Start() {
        BuildUI();
        NewQuestion();
    }

    TMP_Text Text(string value, int size, Transform parent, TextAlignmentOptions align=TextAlignmentOptions.Center) {
        var go = new GameObject(value + "_Text");
        go.transform.SetParent(parent, false);
        var t = go.AddComponent<TextMeshProUGUI>();
        t.text=value; t.fontSize=size; t.alignment=align; t.color=new Color(.18f,.12f,.25f);
        t.fontStyle=FontStyles.Bold;
        return t;
    }

    GameObject Panel(string name, Transform parent, Color color, Vector2 size, Vector2 pos) {
        var go=new GameObject(name);
        go.transform.SetParent(parent,false);
        var img=go.AddComponent<Image>(); img.color=color;
        var rt=go.GetComponent<RectTransform>(); rt.sizeDelta=size; rt.anchoredPosition=pos;
        return go;
    }

    Button Button(string label, Transform parent, Vector2 size, Vector2 pos, Color color) {
        var go=Panel(label+"_Button",parent,color,size,pos);
        var b=go.AddComponent<Button>();
        var txt=Text(label,34,go.transform);
        txt.color=Color.white;
        b.onClick.AddListener(()=>Answer(label));
        return b;
    }

    void BuildUI() {
        var cg=new GameObject("Canvas"); canvas=cg.AddComponent<Canvas>();
        canvas.renderMode=RenderMode.ScreenSpaceOverlay;
        cg.AddComponent<CanvasScaler>().uiScaleMode=CanvasScaler.ScaleMode.ScaleWithScreenSize;
        cg.GetComponent<CanvasScaler>().referenceResolution=new Vector2(1080,1920);
        cg.AddComponent<GraphicRaycaster>();

        Panel("Background",canvas.transform,new Color(.98f,.90f,.96f),new Vector2(1080,1920),Vector2.zero);

        var title=Text("MATH DUEL",72,canvas.transform);
        title.color=Purple; title.rectTransform.anchoredPosition=new Vector2(0,760);

        var sub=Text("Math Fight Between 2 Persons",27,canvas.transform);
        sub.color=new Color(.45f,.25f,.55f); sub.rectTransform.anchoredPosition=new Vector2(0,685);

        Panel("Player1Panel",canvas.transform,new Color(.95f,.55f,.72f),new Vector2(430,150),new Vector2(-230,515));
        Panel("Player2Panel",canvas.transform,new Color(.45f,.65f,1f),new Vector2(430,150),new Vector2(230,515));
        Text("PLAYER 1",28,GameObject.Find("Player1Panel").transform).rectTransform.anchoredPosition=new Vector2(0,30);
        p1Score=Text("0",50,GameObject.Find("Player1Panel").transform); p1Score.rectTransform.anchoredPosition=new Vector2(0,-30); p1Score.color=Color.white;
        Text("PLAYER 2",28,GameObject.Find("Player2Panel").transform).rectTransform.anchoredPosition=new Vector2(0,30);
        p2Score=Text("0",50,GameObject.Find("Player2Panel").transform); p2Score.rectTransform.anchoredPosition=new Vector2(0,-30); p2Score.color=Color.white;

        Panel("QuestionPanel",canvas.transform,Color.white,new Vector2(900,280),new Vector2(0,190));
        question=Text("12 + 8 = ?",68,GameObject.Find("QuestionPanel").transform);
        question.rectTransform.anchoredPosition=Vector2.zero;

        timer=Text("TIME 30",34,canvas.transform); timer.rectTransform.anchoredPosition=new Vector2(0,20); timer.color=Purple;

        Button("18",canvas.transform,Purple,new Vector2(-250,-180),Purple);
        Button("20",canvas.transform,Purple,new Vector2(250,-180),Purple);
        Button("22",canvas.transform,Pink,new Vector2(-250,-340),Pink);
        Button("24",canvas.transform,Pink,new Vector2(250,-340),Pink);

        var start=Panel("StartButton",canvas.transform,new Color(1f,.60f,.15f),new Vector2(520,125),new Vector2(0,-560));
        var sb=start.AddComponent<Button>(); var st=Text("BẮT ĐẦU",40,start.transform); st.color=Color.white;
        sb.onClick.AddListener(Restart);

        status=Text("Chọn đáp án để ghi điểm",25,canvas.transform);
        status.rectTransform.anchoredPosition=new Vector2(0,-700);
        status.color=new Color(.45f,.25f,.55f);
    }

    void NewQuestion() {
        int a=rng.Next(2,20), b=rng.Next(2,20);
        int ans=a+b;
        question.text=$"{a} + {b} = ?";
        question.gameObject.name="QuestionText";
        question.GetComponent<TMP_Text>().SetText($"{a} + {b} = ?");
        currentAnswer=ans;
        status.text="Chọn đáp án để ghi điểm";
    }
    int currentAnswer;
    void Answer(string s) {
        if(int.TryParse(s,out int n)) {
            if(n==currentAnswer){ score1+=10; status.text="Chính xác! +10 điểm"; }
            else { score2+=5; status.text="Chưa đúng – thử lại!"; }
            p1Score.text=score1.ToString(); p2Score.text=score2.ToString();
            NewQuestion();
        }
    }
    void Restart(){score1=0;score2=0;timeLeft=30;p1Score.text="0";p2Score.text="0";NewQuestion();}
    void Update(){
        if(timer==null)return;
        timeLeft-=Time.deltaTime; if(timeLeft<0)timeLeft=0;
        timer.text="TIME "+Mathf.CeilToInt(timeLeft).ToString("00");
        if(timeLeft<=0)status.text="Hết giờ!";
    }
}
