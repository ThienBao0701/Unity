using UnityEngine;
using UnityEngine.UI;
using TMPro;

public class ObjectSeparationUI : MonoBehaviour
{
    void Start(){
        var c=new GameObject("Canvas").AddComponent<Canvas>();
        c.renderMode=RenderMode.ScreenSpaceOverlay;
        var scaler=c.gameObject.AddComponent<CanvasScaler>(); scaler.uiScaleMode=CanvasScaler.ScaleMode.ScaleWithScreenSize; scaler.referenceResolution=new Vector2(1080,1920);
        c.gameObject.AddComponent<GraphicRaycaster>();
        var bg=new GameObject("WhiteBackground"); bg.transform.SetParent(c.transform,false);
        var bi=bg.AddComponent<Image>(); bi.color=Color.white; bg.GetComponent<RectTransform>().sizeDelta=new Vector2(1080,1920);
        Add("TASK 3 – OBJECT SEPARATION",58,c.transform,new Vector2(0,760),new Color(.2f,.15f,.3f));
        Add("Objects are separated into discrete assets",28,c.transform,new Vector2(0,680),Color.gray);
        // Three simple object cards
        Card(c.transform,"OBJECT 01",new Vector2(-300,250),new Color(.92f,.25f,.35f));
        Card(c.transform,"OBJECT 02",new Vector2(0,250),new Color(.15f,.55f,.95f));
        Card(c.transform,"OBJECT 03",new Vector2(300,250),new Color(.95f,.75f,.1f));
        Add("Background removed / transparent asset",30,c.transform,new Vector2(0,-50),new Color(.25f,.25f,.25f));
        Add("Each object can now be imported and positioned independently in Unity.",25,c.transform,new Vector2(0,-150),Color.gray);
    }
    void Add(string s,int size,Transform p,Vector2 pos,Color col){
        var go=new GameObject(s);go.transform.SetParent(p,false);var t=go.AddComponent<TextMeshProUGUI>();
        t.text=s;t.fontSize=size;t.alignment=TextAlignmentOptions.Center;t.color=col;t.fontStyle=FontStyles.Bold;t.rectTransform.anchoredPosition=pos;
    }
    void Card(Transform p,string title,Vector2 pos,Color col){
        var go=new GameObject(title);go.transform.SetParent(p,false);var i=go.AddComponent<Image>();i.color=new Color(.97f,.97f,.97f);
        go.GetComponent<RectTransform>().sizeDelta=new Vector2(250,300);go.GetComponent<RectTransform>().anchoredPosition=pos;
        Add(title,24,go.transform,new Vector2(0,-105),col);
        var shape=new GameObject("SeparatedObject");shape.transform.SetParent(go.transform,false);var si=shape.AddComponent<Image>();si.color=col;
        shape.GetComponent<RectTransform>().sizeDelta=new Vector2(100,150);
    }
}